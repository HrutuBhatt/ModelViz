import "./home.css";
function Home(){
    return (
        <div className="home-container">
          <header className="home-header">
            <h1>📊 Model Viz - Spam Detection</h1>
            <p>An AI-powered spam detection system using ensemble learning.</p>
          </header>
    
          <section className="home-features">
            <h2>🚀 Project Features</h2>
            <ul>
              <li>🔍 Ensemble Learning: Combines GRU, MLP, and XGBoost for better accuracy.</li>
              <li>📈 Real-time Spam Detection: Predicts whether a message is Spam or Ham.</li>
              <li>⚡ User-Defined Training: Customize model parameters (activation, neurons, etc.).</li>
              <li>💾 Analytics for different models.</li>
              <li>👀 Visualizations for preproccessing of Data and Attention Visualization</li>
            </ul>
          </section>
    
        </div>
      );
        
}

export default Home;