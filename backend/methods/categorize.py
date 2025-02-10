from flask import Flask, request, jsonify
import joblib
import re
import nltk
from nltk.corpus import stopwords

# Load the saved model and vectorizer
svm_model = joblib.load(r"D:\ModelViz\backend\pkl_files\category_svm_model.joblib")
vectorizer = joblib.load(r"D:\ModelViz\backend\pkl_files\category_vectorizer.joblib")
label_encoder = joblib.load(r"D:\ModelViz\backend\pkl_files\category_label_encoder.joblib")

# Download stopwords (if not already done)
nltk.download("stopwords")


def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r"\W", " ", text)  # Remove special characters
    text = re.sub(r"\s+", " ", text)  # Remove extra spaces
    text = " ".join([word for word in text.split() if word not in stopwords.words("english")])
    return text


def get_category(text):
    cleaned_text = clean_text(text)
    
    # Convert input text to TF-IDF representation
    text_tfidf = vectorizer.transform([cleaned_text])
    
    # Predict the category
    predicted_label = svm_model.predict(text_tfidf)[0]
    
    # Decode the label (assuming we use LabelEncoder during training)
    category = label_encoder.inverse_transform([predicted_label])[0]
    print(category)
    return category