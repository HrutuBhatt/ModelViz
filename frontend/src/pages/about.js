import React,{useState} from 'react';
import "./about.css";
const About = () => {
    return(
        <>
        <div className="about-container">
            <h1 className="about-title">About Model Viz</h1>
            <h3 className="about-subtitle">
                <b>Model Viz</b> is an AI-powered spam detection system that helps to detect spam texts and visualize how different model work across different parameter.
            </h3>

            <div className="about-section">
                <h2>🚀 Our Mission</h2>
                <p>
                Our goal is to build an advanced <b>spam detection system</b> using 
                    GRU, MLP, and XGBoost with ensemble learning for high accuracy and other models like LSTM, SVM.
                </p>
            </div>

            <div className="about-section">
                <h2>🔹 Technologies Used</h2>
                <ul>
                    <li>TensorFlow/Keras (Deep Learning Models)</li>
                    <li>Scikit Learn, Numpy, Pandas</li>
                    <li>Flask (Backend for Model Training & Prediction)</li>
                    <li>React (Frontend UI)</li>
                </ul>
            </div>

            <div className="about-section">
                <h2>💡 Why Model Viz?</h2>
                <p>
                Model Viz provides custom model training, real-time spam detection, 
                and an interactive UI for AI visualization.
                </p>
            </div>
        </div>
      
      </>
    )

};
export default About;