import React, { useState } from "react";
// import axios from "axios";  // Import axios
import './nn.css';

const NeuralNetwork = () => {
  const [hiddenNeurons, setHiddenNeurons] = useState(64);
  const [activationFunction, setActivationFunction] = useState("relu");
  const [epochs, setEpochs] = useState(10);
  const [learningRate, setLearningRate] = useState(0.001);
  const [loading, setLoading] = useState(false);
  const [accuracy, setAccuracy] = useState(null);
  const [error, setError] = useState("");

  // Function to send parameters to backend
  const handleTrainModel = async () => {
    setLoading(true);
    setError("");
    setAccuracy(null);

    try {
      const response = await fetch("http://127.0.0.1:5000/train", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              hidden_neurons: hiddenNeurons,
              activation_function: activationFunction,
              epochs: epochs,
              learning_rate: learningRate,
            }),
      });
      const data = await response.json();
      if (response.ok) {
        setAccuracy(data.accuracy);
      } else {
        setError("Training failed. Try again.");
      }
    } catch (err) {
      setError("Error connecting to server.");
    }

    setLoading(false);
  };

  return (
    <div className="train-container">
      <h2 className="train-title">Train Neural Network</h2>

      <div className="form-group">
        <label>Hidden Neurons</label>
        <input type="number" value={hiddenNeurons} onChange={(e) => setHiddenNeurons(Number(e.target.value))} />
      </div>

      <div className="form-group">
        <label>Activation Function</label>
        <select value={activationFunction} onChange={(e) => setActivationFunction(e.target.value)}>
          <option value="relu">ReLU</option>
          <option value="sigmoid">Sigmoid</option>
          <option value="tanh">Tanh</option>
        </select>
      </div>

      <div className="form-group">
        <label>Epochs</label>
        <input type="number" value={epochs} onChange={(e) => setEpochs(Number(e.target.value))} />
      </div>

      <div className="form-group">
        <label>Learning Rate</label>
        <input type="number" step="0.0001" value={learningRate} onChange={(e) => setLearningRate(Number(e.target.value))} />
      </div>

      <button onClick={handleTrainModel} disabled={loading} className="nn-button">
        {loading ? "Training... Please wait" : "Train Model"}
      </button>

      {accuracy !== null && <p className="accuracy-text">Training Accuracy: {accuracy.toFixed(4)}</p>}
      {error && <p className="error-text">{error}</p>}
    </div>
  );
};

export default NeuralNetwork;


// import React, { useState } from "react";
// import './nn.css';
// const NeuralNetwork = ()=>{
//   const [hiddenNeurons, setHiddenNeurons] = useState(64);
//   const [activationFunction, setActivationFunction] = useState("relu");
//   const [epochs, setEpochs] = useState(10);
//   const [learningRate, setLearningRate] = useState(0.001);
//   const [loading, setLoading] = useState(false);
//   const [accuracy, setAccuracy] = useState(null);
//   const [error, setError] = useState("");

//       const handleChange = (e) => {
//         setParams({ ...params, [e.target.name]: e.target.value });
//       };
    
//       const handleSubmit = async () => {
//         setLoading(true);
//         try {
//           const response = await fetch("http://127.0.0.1:5000/train", {
//             method: "POST",
//             headers: { "Content-Type": "application/json" },
//             body: JSON.stringify({
//               hidden_neurons: 64,
//               activation_function: "relu",
//               epochs: 10,
//               learning_rate: 0.001,
//             }),
//           });
//           const data = await response.json();
//           setAccuracy(data.accuracy);
//         } catch (error) {
//           console.error("Error training model:", error);
//         }
//         setLoading(false);
//       };
    
//       return (
//         <div className="train-container">
//         <h3 className="train-title">Train Model</h3>
  
//         <div className="form-group">
//           <label>Hidden Neurons</label>
//           <input type="number" name="hidden_neurons" value={params.hidden_neurons} onChange={handleChange} />
//         </div>
  
//         <div className="form-group">
//           <label>Activation Function</label>
//           <select name="activation_function" value={params.activation_function} onChange={handleChange}>
//             <option value="relu">ReLU</option>
//             <option value="sigmoid">Sigmoid</option>
//             <option value="tanh">Tanh</option>
//           </select>
//         </div>
  
//         <div className="form-group">
//           <label>Epochs</label>
//           <input type="number" name="epochs" value={params.epochs} onChange={handleChange} />
//         </div>
  
//         <div className="form-group">
//           <label>Learning Rate</label>
//           <input type="number" step="0.0001" name="learning_rate" value={params.learning_rate} onChange={handleChange} />
//         </div>
  
//         <button onClick={handleSubmit} disabled={loading} >
//           {loading ? "Training... This may take some time..." : "Train Model"}
//         </button>
  
//         {accuracy !== null && <p className="accuracy-text">Training Accuracy: {accuracy}</p>}
//       </div>
  
//     );
// }

// export default NeuralNetwork;