'use client'

import { useState } from 'react'
import TeamForm from './components/team-form'
import RequestForm from './components/request-form'
import ContactForm from './components/contact-form'

export default function Home() {
  const [searchQuery, setSearchQuery] = useState('')

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
        {/* Left Column - Search */}
        <div className="md:col-span-1">
          <div className="sticky top-4">
            <input
              type="search"
              placeholder="Search..."
              className="w-full px-4 py-2 border rounded-lg"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
            />
            {/* Search results would go here */}
          </div>
        </div>

        {/* Right Column - Forms */}
        <div className="md:col-span-2 space-y-8">
          <section className="p-6 border rounded-lg">
            <h2 className="text-2xl font-bold mb-4">Add Team</h2>
            <TeamForm />
          </section>

          <section className="p-6 border rounded-lg">
            <h2 className="text-2xl font-bold mb-4">Add Request</h2>
            <RequestForm />
          </section>

          <section className="p-6 border rounded-lg">
            <h2 className="text-2xl font-bold mb-4">Add Contact</h2>
            <ContactForm />
          </section>
        </div>
      </div>
    </div>
  )
}