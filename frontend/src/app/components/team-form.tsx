'use client'

import { useState } from 'react'
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import * as z from 'zod'

const teamSchema = z.object({
  name: z.string().min(1, 'Team name is required'),
})

export default function TeamForm() {
  const [isSubmitting, setIsSubmitting] = useState(false)

  const { register, handleSubmit, formState: { errors }, reset } = useForm({
    resolver: zodResolver(teamSchema)
  })

  const onSubmit = async (data) => {
    setIsSubmitting(true)
    try {
      const response = await fetch('http://127.0.0.1:8000/api/teams/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      })
      
      if (response.ok) {
        reset()
        // Show success message
        console.log('Team added successfully')
      }
    } catch (error) {
      console.error('Error:', error)
      // Show error message
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      <div>
        <label htmlFor="name" className="block text-sm font-medium mb-1">Team Name</label>
        <input
          id="name"
          {...register('name')}
          className="w-full px-3 py-2 border rounded-lg"
          type="text"
        />
        {errors.name && (
          <p className="text-red-500 text-sm mt-1">{errors.name.message}</p>
        )}
      </div>

      <button
        type="submit"
        disabled={isSubmitting}
        className="w-full bg-blue-500 text-white py-2 px-4 rounded-lg hover:bg-blue-600 disabled:opacity-50"
      >
        {isSubmitting ? 'Submitting...' : 'POST'}
      </button>
    </form>
  )
}