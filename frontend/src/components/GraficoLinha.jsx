import React from "react";
import { LineChart, Line, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from "recharts";

export default function GraficoLinha({ dados }) {
  return (
    <div style={{ marginBottom: 40 }}>
      <h3>Beneficiários e Valor Pago</h3>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={dados}>
          <XAxis dataKey="mes_competencia" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="total_beneficiarios" stroke="#8884d8" name="Beneficiários" />
          <Line type="monotone" dataKey="total_pago" stroke="#82ca9d" name="Valor Pago (R$)" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
