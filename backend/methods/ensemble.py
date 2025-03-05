from tensorflow.keras.models import load_model
from methods.categorize import clean_text
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import joblib
import re
from nltk.corpus import stopwords
import nltk
# Load Models
gru_model = load_model(r"D:\ModelViz\backend\pkl_files\gru_model.keras")
mlp_model = load_model(r"D:\ModelViz\backend\pkl_files\mlp_model.keras")
autoencoder = load_model(r"D:\ModelViz\backend\pkl_files\autoencoder.keras")
xgb_model = joblib.load(r"D:\ModelViz\backend\pkl_files\xgboost_model.pkl")
tokenizer = joblib.load(r"D:\ModelViz\backend\pkl_files\tokenizer.joblib")
encoder = load_model(r"D:\ModelViz\backend\pkl_files\encoder.keras")
tfidf_vectorizer = joblib.load(r"D:\ModelViz\backend\pkl_files\tfidf_vectorizer.joblib")
count_vectorizer = joblib.load(r"D:\ModelViz\backend\pkl_files\count_vectorizer.joblib")
def ensemble_predict(text):
    # Preprocess input
    text_cleaned = clean_text(text)
    
    # Vectorization
    text_tfidf = tfidf_vectorizer.transform([text_cleaned]).toarray()
    text_count = count_vectorizer.transform([text_cleaned]).toarray()
    text_seq = pad_sequences(tokenizer.texts_to_sequences([text_cleaned]), maxlen=50)
    
    # Model Predictions
    p1 = gru_model.predict(text_seq)[0][0]
    p2 = mlp_model.predict(text_tfidf)[0][0]
    
    # Autoencoder + XGBoost
    text_encoded = encoder.predict(text_count)
    p3 = xgb_model.predict(text_encoded)[0]

    # Majority Voting
    final_prediction = round((p1 + p2 + p3) / 3)
    
    return final_prediction #1 or 0
