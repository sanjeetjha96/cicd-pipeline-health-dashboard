import React, {useEffect, useState} from 'react'
import axios from 'axios'

const API_BASE = import.meta.env.VITE_API_BASE ? import.meta.env.VITE_API_BASE : 'http://localhost:8000'

export default function Dashboard(){
  const [metrics, setMetrics] = useState(null)
  const [runs, setRuns] = useState([])

  async function fetchMetrics(){
    try{ const r = await axios.get(`${API_BASE}/api/metrics`); setMetrics(r.data) }catch(e){ console.error(e) }
  }
  async function fetchRuns(){
    try{ const r = await axios.get(`${API_BASE}/api/runs`); setRuns(r.data) }catch(e){ console.error(e) }
  }

  useEffect(()=>{ fetchMetrics(); fetchRuns(); const id = setInterval(()=>{ fetchMetrics(); fetchRuns(); }, 30000); return ()=> clearInterval(id) },[])

  return (
    <div>
      <div className="grid grid-cols-3 gap-4 mb-6">
        <Tile title="Total runs">{metrics ? metrics.total_runs : '—'}</Tile>
        <Tile title="Success">{metrics ? metrics.success_count : '—'}</Tile>
        <Tile title="Failures">{metrics ? metrics.failure_count : '—'}</Tile>
      </div>

      <div className="mb-4">
        <h2 className="text-xl mb-2">Recent Runs</h2>
        <div>
          {runs.length===0 && <div>No runs yet</div>}
          {runs.map(r=> (
            <div key={r.id} className="p-2 border mb-2 rounded">
              <div><strong>Run:</strong> {r.run_id} — {r.conclusion || r.status}</div>
              <div><small>{r.html_url}</small></div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

function Tile({title, children}){
  return (
    <div className="p-4 border rounded shadow-sm">
      <div className="text-sm text-gray-500">{title}</div>
      <div className="text-2xl font-bold">{children}</div>
    </div>
  )
}
