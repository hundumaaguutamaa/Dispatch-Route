'use client'

import { useState } from 'react'
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import * as z from 'zod'

const contactSchema = z.object({
  name: z.string().min(1, 'Name is required'),
  email: z.string().email('Invalid email address'),
  phone: z.string().min(1, 'Phone is required'),
  officeLocation: z.string().min(1, 'Office location is required'),
  team: z.string().min(1, 'Team is required'),
})

export default function ContactForm() {
  const [isSubmitting, setIsSubmitting] = useState(false)

  const { register, handleSubmit, formState: { errors }, reset } = useForm({
    resolver: zodResolver(contactSchema)
  })

  const onSubmit = async (data) => {
    setIsSubmitting(true)
    try {
      const response = await fetch('http://127.0.0.1:8000/api/contacts/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      })
      
      if (response.ok) {
        reset()
        // Show success message
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
        <label className="block text-sm font-medium mb-1">Name</label>
        <input
          {...register('name')}
          className="w-full px-3 py-2 border rounded-lg"
          type="text"
        />
        {errors.name && (
          <p className="text-red-500 text-sm mt-1">{errors.name.message}</p>
        )}
      </div>

      <div>
        <label className="block text-sm font-medium mb-1">Email</label>
        <input
          {...register('email')}
          className="w-full px-3 py-2 border rounded-lg"
          type="email"
        />
        {errors.email && (
          <p className="text-red-500 text-sm mt-1">{errors.email.message}</p>
        )}
      </div>

      <div>
        <label className="block text-sm font-medium mb-1">Phone</label>
        <input
          {...register('phone')}
          className="w-full px-3 py-2 border rounded-lg"
          type="tel"
        />
        {errors.phone && (
          <p className="text-red-500 text-sm mt-1">{errors.phone.message}</p>
        )}
      </div>

      <div>
        <label className="block text-sm font-medium mb-1">Office Location</label>
        <input
          {...register('officeLocation')}
          className="w-full px-3 py-2 border rounded-lg"
          type="text"
        />
        {errors.officeLocation && (
          <p className="text-red-500 text-sm mt-1">{errors.officeLocation.message}</p>
        )}
      </div>

      <div>
        <label className="block text-sm font-medium mb-1">Team</label>
        <select
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