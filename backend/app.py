from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
from models.svm import predict_spam as predict_svm
# from models.naive_bayes import predict_spam as predict_naive_bayes
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Function to load model based on user selection
def load_model(model_name):
    model_path = os.path.join("models", f"{model_name}_model.pkl")
    vectorizer_path = os.path.join("models", f"{model_name}_vectorizer.pkl")
    
    if not os.path.exists(model_path) or not os.path.exists(vectorizer_path):
        return None, None
    
    # Load the model and vectorizer
    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)
        
    with open(vectorizer_path, "rb") as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
        
    return model, vectorizer

# Define the spam prediction route
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json  # Get JSON data from the frontend
    text = data.get("text", "")  # Extract the text to predict
    model_name = data.get("model", "svm")  # Extract the selected model

    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    # Load the selected model dynamically
    model, vectorizer = load_model(model_name)

    if model is None or vectorizer is None:
        return jsonify({"error": f"Model '{model_name}' not found"}), 400

    # Call the appropriate prediction function based on the model
    if model_name == "svm":
        result = predict_svm(model, vectorizer, text)
    elif model_name == "naive_bayes":
        result = predict_naive_bayes(model, vectorizer, text)
    elif model_name == "logistic_regression":
        result = predict_log_reg(model, vectorizer, text)
    else:
        return jsonify({"error": "Invalid model selected"}), 400

    return jsonify({"result": "Spam" if result == 1 else "Not Spam"})

if __name__ == "__main__":
    app.run(debug=True)
