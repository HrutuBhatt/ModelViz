import { useState } from "react";
const Vectorize = ({stemmedText})=>{
    const [result, setResult] = useState('');
    
    const handleSubmit = async() => {
        try {
            const response = await fetch('http://127.0.0.1:5000/vectorize', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({
                text: stemmedText,
              }),
            });
      
            const data = await response.json();
            if (response.ok) {
              setResult(data); // Display the result
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
            <button onClick={handleSubmit}>Vectorize</button>
            {result && <p>Result: {result}</p>}
        </div>
    )
}
export default Vectorize;