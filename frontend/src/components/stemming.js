import React, { useState } from "react";

const Stemming = ({message, setMessage, stemmedText, setStemmedText})=>{
    // const [message, setMessage] = useState(sharedText);
    const [result, setResult] = useState('');
    const [selectedStemmer, setSelectedStemmer] = useState('PS');
    
    const handleSubmit = async() => {
        try {
            const response = await fetch('http://127.0.0.1:5000/stemming', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({
                stemmer: selectedStemmer,
                text: message,
              }),
            });
      
            const data = await response.json();
            if (response.ok) {
              setResult(data); // Display the result
              setStemmedText(data.toString())
            } else {
              setResult(`Error: ${data.error}`);
            }
        } catch (error) {
            setResult(`Error: ${error.message}`);
        }
    }
    return(
        <div>
            <h2>Enter text to Visualize Stemming</h2>
            <textarea
                placeholder="Enter your message"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
            />
            <br />
            <select
                value={selectedStemmer}
                onChange={(e) => setSelectedStemmer(e.target.value)}
            >
                <option value="PS">Porter Stemmer</option>
                <option value="SBS">Snowball Stemmer</option>
                <option value="LS">Lancaster Stemmer</option>
               
            </select>
            <button onClick={handleSubmit}>Stem</button>
            {result && <p>Result: {result}</p>}
        </div>
    )
}

export default Stemming;