import { useState } from 'react'
import { AdminDashboardView } from './views/admin/AdminDashboardView'
import { GuestDealsView } from './views/guest/GuestDealsView'
import { TravelerTripsView } from './views/traveler/TravelerTripsView'
import './App.css'

type Role = 'guest' | 'traveler' | 'admin'

function App() {
  const [activeRole, setActiveRole] = useState<Role>('guest')

  return (
    <main>
      <h1>Travel Planner</h1>
      <section aria-label='Role shell'>
        <nav aria-label='Role navigation'>
          <button type='button' onClick={() => setActiveRole('guest')}>
            Guest
          </button>
          <button type='button' onClick={() => setActiveRole('traveler')}>
            Traveler
          </button>
          <button type='button' onClick={() => setActiveRole('admin')}>
            Admin
          </button>
        </nav>

        {activeRole === 'guest' && <GuestDealsView />}
        {activeRole === 'traveler' && <TravelerTripsView />}
        {activeRole === 'admin' && <AdminDashboardView />}
      </section>
    </main>
  )
}

export default App
