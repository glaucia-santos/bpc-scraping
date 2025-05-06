import React from "react";

export default function Filtros({ estado, setEstado, cidade, setCidade, cidades, estados, periodo, setPeriodo }) {
  return (
    <div style={{ marginBottom: 20 }}>
      <label>Estado: </label>
      <select value={estado} onChange={(e) => setEstado(e.target.value)}>
        <option value="">Selecione</option>
        {estados.map((uf) => (
          <option key={uf} value={uf}>{uf}</option>
        ))}
      </select>
      <label style={{ marginLeft: 10 }}>Cidade: </label>
      <select value={cidade} onChange={(e) => setCidade(e.target.value)}>
        <option value="">Todas</option>
        {cidades.map((m) => (
          <option key={m} value={m}>{m}</option>
        ))}
      </select>
      <label style={{ marginLeft: 10 }}>Período: </label>
      <input type="date" value={periodo[0]} onChange={(e) => setPeriodo([e.target.value, periodo[1]])} />
      <input type="date" value={periodo[1]} onChange={(e) => setPeriodo([periodo[0], e.target.value])} />
    </div>
  );
}
