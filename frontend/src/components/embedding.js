import React, { useState } from "react";
import Plot from "react-plotly.js";
import Papa from "papaparse";

const EmbeddingVisualization = () => {
  const [csvData, setCsvData] = useState([]);
  const [xValues, setXValues] = useState([]);
  const [yValues, setYValues] = useState([]);

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (!file) return;

    Papa.parse(file, {
      header: true, // Assumes the first row is the header
      skipEmptyLines: true,
      complete: (result) => {
        const data = result.data;
        setCsvData(data);

        // Assuming your CSV has columns "x" and "y" for embeddings
        const x = data.map((row) => parseFloat(row.x));
        const y = data.map((row) => parseFloat(row.y));

        setXValues(x);
        setYValues(y);
      },
      error: (error) => {
        console.error("Error reading CSV file:", error);
      },
    });
  };

  return (
    <div>
      <h1>Embedding Plotter</h1>
      <input
        type="file"
        accept=".csv"
        onChange={handleFileUpload}
        style={{ marginBottom: "20px" }}
      />
      {xValues.length > 0 && yValues.length > 0 ? (
        <Plot
          data={[
            {
              x: xValues,
              y: yValues,
              mode: "markers",
              type: "scatter",
              marker: { size: 8, color: "blue" },
            },
          ]}
          layout={{
            title: "Embeddings Visualization",
            xaxis: { title: "X-Axis (Embedding Dimension 1)" },
            yaxis: { title: "Y-Axis (Embedding Dimension 2)" },
            height: 500,
          }}
          style={{ width: "100%", height: "100%" }}
        />
      ) : (
        <p>Please upload a CSV file to visualize the embeddings.</p>
      )}
    </div>
  );
};

export default EmbeddingVisualization;
