import Image from 'next/image'
import Link from 'next/link'
import { Monitor } from 'lucide-react'

export default function Header() {
  return (
    <header className="border-b">
      <div className="container mx-auto px-4 h-16 flex items-center justify-between">
        <Link href="/" className="flex items-center space-x-2">
          <Monitor className="h-6 w-6" />
          <span className="font-bold text-xl">IT Service Desk</span>
        </Link>
        <nav className="space-x-4">
          <Link href="/teams" className="hover:text-primary">Teams</Link>
          <Link href="/requests" className="hover:text-primary">Requests</Link>
          <Link href="/contacts" className="hover:text-primary">Contacts</Link>
        </nav>
      </div>
    </header>
  )
}