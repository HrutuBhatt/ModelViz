import { useState } from "react";
import Plot from 'react-plotly.js';

const Vectorize = ({stemmedText})=>{
    const [result, setResult] = useState('');
    const [plotData, setPlotData] = useState(null);

    const handleSubmit = async() => {
        try {
            const response = await fetch('http://127.0.0.1:5000/vectorize', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({
                sentences: stemmedText.split('\n')
              }),
            });
      
            const data = await response.json();
            if (response.ok) {
              const tfidfValues = data.tfidf_values;
              const words = data.words;
              const sentences = data.sentences;

              const plot = {
                z: tfidfValues,
                x: words,
                y: sentences,
                type: 'heatmap',
                colorscale: 'Viridis',
              };

              setPlotData(plot);
            } else {
              setResult(`Error: ${data.error}`);
            }
        } catch (error) {
            setResult(`Error: ${error.message}`);
        }
    }
    return (
        <div>
            <h2>Vectorize the text</h2>
            <button onClick={handleSubmit} className="btn-svm">Vectorize</button>
            {result && <p>Result: {result}</p>}
            {plotData && (
              <Plot
                data={[plotData]}
                layout={{
                  title: 'TF-IDF Heatmap',
                  xaxis: { title: 'Words' },
                  yaxis: { title: 'Sentences' },
                }}
              />
            )}
            <div>
              <br/>
            <li>  High TF-IDF Value: If a word has a high TF-IDF value in a sentence, it means that the word is significant in that sentence (it appears frequently in the sentence, but not across other sentences, making it more unique to that sentence).</li><br/>
            <li>  Low TF-IDF Value: A low TF-IDF value indicates that a word is common across all sentences and doesn't provide much distinction to any particular sentence.</li>
            <br/>
            </div>
        </div>
    )
}
export default Vectorize;