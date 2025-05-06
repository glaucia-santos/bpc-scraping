import React from "react";

export default function PainelDiscrepantes({ dados }) {
  return (
    <div>
      <h3>Registros com Pagamentos Discrepantes</h3>
      <table border="1" cellPadding={5}>
        <thead>
          <tr>
            <th>UF</th>
            <th>Município</th>
            <th>Data</th>
            <th>Valor Pago</th>
            <th>Beneficiários</th>
          </tr>
        </thead>
        <tbody>
          {dados.map((row, idx) => (
            <tr key={idx}>
              <td>{row.uf}</td>
              <td>{row.municipio}</td>
              <td>{row.mes_competencia}</td>
              <td>R$ {parseFloat(row.valor_pago).toLocaleString("pt-BR")}</td>
              <td>{row.quantidade_beneficiarios}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
