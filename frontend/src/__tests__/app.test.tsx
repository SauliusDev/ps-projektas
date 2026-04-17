import { fireEvent, render, screen } from '@testing-library/react'
import { describe, expect, it } from 'vitest'
import App from '../App'

describe('App role shell', () => {
  it('renders role shell boundary controls and guest view by default', () => {
    render(<App />)

    expect(screen.getByRole('region', { name: 'Role shell' })).toBeInTheDocument()
    expect(screen.getByRole('button', { name: 'Guest' })).toBeInTheDocument()
    expect(screen.getByRole('button', { name: 'Traveler' })).toBeInTheDocument()
    expect(screen.getByRole('button', { name: 'Admin' })).toBeInTheDocument()
    expect(screen.getByText('Guest Deals')).toBeInTheDocument()
  })

  it('switches boundary view by selected role', () => {
    render(<App />)

    fireEvent.click(screen.getByRole('button', { name: 'Traveler' }))
    expect(screen.getByText('Traveler Trips')).toBeInTheDocument()

    fireEvent.click(screen.getByRole('button', { name: 'Admin' }))
    expect(screen.getByText('Admin Dashboard')).toBeInTheDocument()

    fireEvent.click(screen.getByRole('button', { name: 'Guest' }))
    expect(screen.getByText('Guest Deals')).toBeInTheDocument()
  })
})
