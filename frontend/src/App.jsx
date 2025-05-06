import React, { useEffect, useState } from 'react'
import axios from 'axios'

function App() {
  const [status, setStatus] = useState('carregando...')

  useEffect(() => {
    axios.get(`${import.meta.env.VITE_API_URL}/api/status/`)
      .then((res) => setStatus(res.data.status))
      .catch(() => setStatus('erro'))
  }, [])

  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial' }}>
      <h1>Projeto BPC</h1>
      <p>Status da API: {status}</p>
    </div>
  )
}

export default App
