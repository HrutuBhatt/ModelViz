from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import re
from models.svm import predict_spam as predict_svm
from methods.lstm_method import classify_message
# from models.naive_bayes import predict_spam as predict_naive_bayes
import os
from models.vectorizer import vectorize_text, preprocess_text
from methods.nb_method import predict_spam_nb
# Initialize Flask app
app = Flask(__name__)
CORS(app)
svm_model = joblib.load('./svm_joblib.pkl')

# Define the spam prediction route


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json  # Get JSON data from the frontend
    text = data.get('text')  # Extract the text to predict
    model_name = data.get("model")  # Extract the selected model
    
    preprocessed_text = preprocess_text(text)
    vectorized_text = vectorize_text(preprocessed_text)
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    # Load the selected model dynamically
    if model_name is None :
        return jsonify({"error": f"Model '{model_name}' not found"}), 400
    if model_name=='svm':
        prediction = svm_model.predict(vectorized_text)[0]
        print(prediction)
        return jsonify({"prediction": "spam" if prediction == 1 else "ham"})
    elif model_name=='lstm':
        result = classify_message(text)
        return jsonify({"prediction": "ham" if result == 0 else "spam"})
    elif model_name=='nb':
        result = predict_spam_nb(text)
        return jsonify({"prediction": "ham" if result == 0 else "spam"})

    else:
        return jsonify({"error": "Model not supported"})

    

    # Call the appropriate prediction function based on the model
    
if __name__ == "__main__":
    app.run(debug=True)
