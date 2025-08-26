import React from 'react'
import Dashboard from './components/Dashboard'
export default function App(){
  return (
    <div className="p-4 font-sans">
      <h1 className="text-2xl mb-4">CI/CD Pipeline Health Dashboard</h1>
      <Dashboard />
    </div>
  )
}
