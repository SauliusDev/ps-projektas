import { render, screen } from '@testing-library/react'
import { describe, expect, it } from 'vitest'
import App from '../App'

describe('App role shell', () => {
  it('renders role shell boundary controls', () => {
    render(<App />)

    expect(screen.getByRole('region', { name: 'Role shell' })).toBeInTheDocument()
    expect(screen.getByRole('button', { name: 'Guest' })).toBeInTheDocument()
    expect(screen.getByRole('button', { name: 'Traveler' })).toBeInTheDocument()
    expect(screen.getByRole('button', { name: 'Admin' })).toBeInTheDocument()
  })
})
