import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [status, setStatus] = useState('');

  useEffect(() => {
    axios.get(`${import.meta.env.VITE_API_URL}/api/status/`)
      .then(res => setStatus(res.data.status))
      .catch(() => setStatus('erro'));
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold">Projeto BPC</h1>
      <p>Status da API: {status}</p>
    </div>
  );
}

export default App;
