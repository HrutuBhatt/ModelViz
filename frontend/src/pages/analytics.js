import React, { useEffect, useState } from 'react';
import { Bar } from 'react-chartjs-2';
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend,
} from 'chart.js';
ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

const Analytics = () => {
    const [chartData, setChartData] = useState(null);

    useEffect(() => {
        const fetchMetrics = async () => {
            try {
                const response = await fetch('http://127.0.0.1:5000/analytics');
                const data = await response.json();

                // Prepare data for chart
                const models = Object.keys(data); // ["SVM", "Naive Bayes", "LSTM"]
                const metrics = ["accuracy", "precision", "recall", "f1"];

                const datasets = metrics.map((metric, index) => ({
                    label: metric,
                    backgroundColor: `rgba(${(index + 1) * 50}, ${100 + index * 50}, ${150 - index * 30}, 0.6)`,
                    borderColor: `rgba(${(index + 1) * 50}, ${100 + index * 50}, ${150 - index * 30}, 1)`,
                    borderWidth: 1,
                    data: models.map((model) => data[model][metric]),
                }));

                setChartData({
                    labels: models, // X-axis labels (models)
                    datasets,
                });
            } catch (error) {
                console.error('Error fetching metrics:', error);
            }
        };

        fetchMetrics();
    }, []);

    return(
        <div>
            <h1 style={{alignItems: "center"}}>Model Metrics Bar Graph</h1>
              
                {chartData ? (
                    <Bar
                        data={chartData}
                        options={{
                            responsive: true,
                            scales: {
                                x: { stacked: true },
                                y: { beginAtZero: true },
                            },
                        }}
                        width={150} // Chart width in pixels
                        height={50}
                    />
                ) : (
                    <p>Loading...</p>
                )}
            
        </div>
    )
}
export default Analytics;