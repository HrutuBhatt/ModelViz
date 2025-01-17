import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/navbar'; 
import Home from './pages/home';
import About from './pages/about';
import DetectSpam from './pages/detectspam';
function App() {
  return (
    <>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/detectspam" element={<DetectSpam />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
