import { useEffect, useState } from 'react'
import axios from 'axios'

function App() {
  const [status, setStatus] = useState('carregando...')

  useEffect(() => {
    const apiUrl = import.meta.env.VITE_API_URL
    if (!apiUrl) {
      setStatus('erro (VITE_API_URL não definida)')
      return
    }

    axios.get(`${apiUrl}/api/status/`)
      .then((res) => {
        if (res.status === 200 && res.data.status === 'online') {
          setStatus('online')
        } else {
          setStatus('erro (resposta inesperada)')
        }
      })
      .catch((error) => {
        console.error('Erro ao conectar com a API:', error)
        setStatus('erro (API indisponível)')
      })
  }, [])

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h1>Projeto BPC</h1>
      <p>Status da API: <strong>{status}</strong></p>
    </div>
  )
}

export default App
