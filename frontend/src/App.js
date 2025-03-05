import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/navbar'; 
import Home from './pages/home';
import About from './pages/about';
import DetectSpam from './pages/detectspam';
import Analytics from './pages/analytics';
import SVM from './pages/svm_viz';
import LSTM from './pages/lstm_viz';
import Undersampling from './pages/undersampling';
import NeuralNetwork from './pages/neuralnetwork';
function App() {
  return (
    <>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/detectspam" element={<DetectSpam />} />
          <Route path="/analytics" element={<Analytics />} />
          <Route path="/svm" element={<SVM />} />
          <Route path="/nn" element={<NeuralNetwork />} />
          <Route path="/lstm" element={<LSTM />} />
          <Route path="/lr" element={<Analytics />} />
          <Route path="/undersample" element={<Undersampling />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
