from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import re
# from models.svm import predict_spam as predict_svm
from methods.lstm_method import classify_message
import os
from models.vectorizer import vectorize_text, preprocess_text, explain_prediction
from methods.nb_method import predict_spam_nb
from methods.get_metrics import get_metrics
from methods.preprocess import stemtext
from methods.categorize import get_category
from sklearn.feature_extraction.text import TfidfVectorizer
from models.neuralnetwork import train_nn
from methods.ensemble import ensemble_predict
# Initialize Flask app
app = Flask(__name__)

CORS(app)
svm_model = joblib.load('./svm_joblib.pkl')
lr_model = joblib.load('./logistic_regression.pkl')

# Define the spam prediction route


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json  # Get JSON data from the frontend
    text = data.get('text')  # Extract the text to predict
    model_name = data.get("model")  # Extract the selected model
    print(text, model_name)
    preprocessed_text = preprocess_text(text)
    vectorized_text = vectorize_text(preprocessed_text)
    result = explain_prediction(text)
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    # Load the selected model dynamically
    if model_name is None :
        return jsonify({"error": f"Model '{model_name}' not found"}), 400
    if model_name=='svm':
        prediction = svm_model.predict(vectorized_text)[0]
        print(prediction)
        return jsonify({"prediction": "spam" if prediction == 1 else "ham", "result": result})
    elif model_name=='lr':
        prediction = lr_model.predict(vectorized_text)[0]
        print(prediction)
        return jsonify({"prediction": "spam" if prediction == 1 else "ham", "result": result})
    elif model_name=='lstm':
        prediction = classify_message(text)
        return jsonify({"prediction": "ham" if prediction == 0 else "spam", "result": result})
    elif model_name=='nb':
        prediction = predict_spam_nb(text)
        return jsonify({"prediction": "ham" if prediction == 0 else "spam", "result": result})
    elif model_name=='hybrid':
        prediction = ensemble_predict(text)
        return jsonify({"prediction": "ham" if prediction == 0 else "spam", "result": result})
    else:
        return jsonify({"error": "Model not supported"})

    

#get analysis of metrics of different models
@app.route("/analytics", methods=["GET"])
def analytics():
    metrics = get_metrics()
    # print(metrics)
    return jsonify(metrics)

@app.route("/stemming", methods=["POST"])
def stem():
    data = request.json  # Get JSON data from the frontend
    text = data.get('text')  # Extract the text to predict
    stemfunc = data.get("stemmer")  # Extract the selected stemmer
    output = stemtext(text, stemfunc)
    return jsonify(output)

@app.route('/vectorize', methods=['POST'])
def vectorize_text_view():
    # Get text from the request body
    data = request.json
    sentences = data.get('sentences', [])
    
    # Initialize TF-IDF Vectorizer
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(sentences)
    
    # Convert the TF-IDF matrix to a list of dictionaries for easier handling in React
    tfidf_matrix = X.toarray()
    words = vectorizer.get_feature_names_out()
    
    result = {
        'words': words.tolist(),
        'tfidf_values': tfidf_matrix.tolist(),
        'sentences': sentences
    }
    
    return jsonify(result)


@app.route('/category', methods=['POST'])
def find_category():
    data = request.json
    text = data.get('text')
    category = get_category(text)
    return jsonify(category)


# @app.route('/embeddings', methods=['GET'])
# def get_embeddings():
#     return embedding_df.to_json(orient="records")

@app.route('/train', methods=["POST"])
def train_model():
    data = request.json
    hidden_neurons = data.get("hidden_neurons", 64)
    activation_function = data.get("activation_function", "relu")
    epochs = data.get("epochs", 10)
    learning_rate = data.get("learning_rate", 0.001)
    accuracy = train_nn(hidden_neurons, activation_function, epochs, learning_rate)
    return  jsonify({"message": "Model trained successfully", "accuracy": accuracy})


if __name__ == "__main__":
    app.run(debug=True)
