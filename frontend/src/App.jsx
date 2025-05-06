import React, { useEffect, useState } from "react";
import axios from "axios";
import Filtros from "./components/Filtros";
import GraficoLinha from "./components/GraficoLinha";
import PainelDiscrepantes from "./components/PainelDiscrepantes";

const API = import.meta.env.VITE_API_URL;

export default function App() {
  const [estado, setEstado] = useState("");
  const [cidade, setCidade] = useState("");
  const [cidades, setCidades] = useState([]);
  const [estados, setEstados] = useState([]);
  const [dados, setDados] = useState([]);
  const [discrepantes, setDiscrepantes] = useState([]);
  const [periodo, setPeriodo] = useState(["2023-01-01", "2023-12-31"]);

  useEffect(() => {
    axios.get(`${API}/bpc/estados/`).then((res) => setEstados(res.data));
    axios.get(`${API}/bpc/discrepantes/`).then((res) => setDiscrepantes(res.data));
  }, []);

  useEffect(() => {
    if (estado) {
      axios.get(`${API}/bpc/cidades/?uf=${estado}`).then((res) => setCidades(res.data));
    }
  }, [estado]);

  useEffect(() => {
    const url = `${API}/bpc/analise/?uf=${estado}&municipio=${cidade}&periodo=${periodo[0]},${periodo[1]}`;
    axios.get(url).then((res) => setDados(res.data));
  }, [estado, cidade, periodo]);

  return (
    <div style={{ fontFamily: "Arial", padding: 20 }}>
      <h1>Projeto BPC</h1>
      <Filtros
        estado={estado}
        setEstado={setEstado}
        cidade={cidade}
        setCidade={setCidade}
        cidades={cidades}
        estados={estados}
        periodo={periodo}
        setPeriodo={setPeriodo}
      />
      <GraficoLinha dados={dados} />
      <PainelDiscrepantes dados={discrepantes} />
    </div>
  );
}
