import React, { useState } from 'react';

const DetectSpam = () => {
  const [message, setMessage] = useState('');
  const [selectedModel, setSelectedModel] = useState('svm');
  const [result, setResult] = useState('');

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
      } else {
        setResult(`Error: ${data.error}`);
      }
    } catch (error) {
      setResult(`Error: ${error.message}`);
    }
  };

  return (
    <div>
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
        <option value="svm">Naive Bayes</option>
        <option value="svm">LSTM</option>
        <option value="svm">Logistic Regression</option>
        <option value="svm">BERT</option>
        {/* Add more models here if needed */}
      </select>
      <br />
      <button onClick={handleSubmit}>Check Spam</button>
      {result && <p>Result: {result}</p>}
    </div>
  );
};

export default DetectSpam;
