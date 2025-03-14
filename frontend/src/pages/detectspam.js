import React, { useState } from 'react';
import './detectspam.css';
const DetectSpam = () => {
  const [message, setMessage] = useState('');
  const [selectedModel, setSelectedModel] = useState('svm');
  const [result, setResult] = useState('');
  const [highlightedMessage, setHighlightedMessage] = useState('');
  const [category, setCategory] = useState('');
  const handleSubmit = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          model: selectedModel,
          text: message,
        }),
      });

      const data = await response.json();
      if (response.ok) {
        setResult(data.prediction); // Display the result
        const { top_contributing_words } = data.result;
        let updatedMessage = message;
        top_contributing_words.forEach((item) => {
          const word = item.word;
          const importance = item.importance.toFixed(4); // Format importance
          const regex = new RegExp(`\\b${word}\\b`, 'gi'); // To match the whole word, case-insensitive

          // Wrap the word in a span with a tooltip for importance
          updatedMessage = updatedMessage.replace(
            regex,
            `<span class="highlighted-word"  title="Importance: ${importance}">
              ${word} (${importance})
            </span>`
          );
        });
        setHighlightedMessage(updatedMessage);
      } else {
        setResult(`Error: ${data.error}`);
      }
    } catch (error) {
      setResult(`Error: ${error.message}`);
    }
  };

  const checkCategory = async()=>{
    try{
      const response = await fetch('http://127.0.0.1:5000/category', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          text: message,
        }),
      });

      const data = response.json();
      setCategory(data);
    }
    catch(error){
      setResult(`Error: ${error.message}`);
    }
  }
  return (
    <div className='main'>
    <div className='container'>
      <h1>Spam Detector</h1>
      <textarea
        placeholder="Enter your message"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <br />
      <select
        value={selectedModel}
        onChange={(e) => setSelectedModel(e.target.value)}
      >
        <option value="svm">SVM</option>
        <option value="nb">Naive Bayes</option>
        <option value="lstm">LSTM</option>
        <option value="svm">Logistic Regression</option>
        <option value="hybrid">Hybrid</option>
        {/* Add more models here if needed */}
      </select>
      <br />
      <button onClick={handleSubmit}>Check Spam</button>
      
      {result && <p>Result: {result}</p>}
      
      {/* Display the highlighted message with importance */}
      {highlightedMessage && (
        <div>
          <h3>Highlighted Message:</h3>
          <p dangerouslySetInnerHTML={{ __html: highlightedMessage }}></p>
        </div>
      )}
   
    {/* to know category of spam text (using svm) */}
    <h3>Check category of your spam text: </h3>
    <button onClick={checkCategory}>Category</button>
    <p>Spam text belongs to:<b>{category}</b></p>
    </div>
    </div>
  );
};

export default DetectSpam;
