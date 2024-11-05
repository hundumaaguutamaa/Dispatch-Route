'use client'

import { useState } from 'react'
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import * as z from 'zod'

const requestSchema = z.object({
  title: z.string().min(1, 'Title is required'),
  description: z.string().min(1, 'Description is required'),
  team: z.string().min(1, 'Team is required'),
})

export default function RequestForm() {
  const [isSubmitting, setIsSubmitting] = useState(false)

  const { register, handleSubmit, formState: { errors }, reset } = useForm({
    resolver: zodResolver(requestSchema)
  })

  const onSubmit = async (data) => {
    setIsSubmitting(true)
    try {
      const response = await fetch('http://127.0.0.1:8000/api/requests/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      })
      
      if (response.ok) {
        reset()
        // Show success message
        console.log('Request submitted successfully')
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
        <label htmlFor="title" className="block text-sm font-medium mb-1">Title</label>
        <input
          id="title"
          {...register('title')}
          className="w-full px-3 py-2 border rounded-lg"
          type="text"
        />
        {errors.title && (
          <p className="text-red-500 text-sm mt-1">{errors.title.message}</p>
        )}
      </div>

      <div>
        <label htmlFor="description" className="block text-sm font-medium mb-1">Description</label>
        <textarea
          id="description"
          {...register('description')}
          className="w-full px-3 py-2 border rounded-lg"
          rows={4}
        />
        {errors.description && (
          <p className="text-red-500 text-sm mt-1">{errors.description.message}</p>
        )}
      </div>

      <div>
        <label htmlFor="team" className="block text-sm font-medium mb-1">Team</label>
        <select
          id="team"
          {...register('team')}
          className="w-full px-3 py-2 border rounded-lg"
        >
          <option value="">Select a team</option>
          <option value="IT Service Desk Level I">IT Service Desk Level I</option>
          {/* Add more options as needed */}
        </select>
        {errors.team && (
          <p className="text-red-500 text-sm mt-1">{errors.team.message}</p>
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