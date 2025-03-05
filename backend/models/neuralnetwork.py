import pandas as pd
import joblib
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import nltk
import re
from methods.categorize import clean_text
from nltk.corpus import stopwords

df = pd.read_csv(r'D:\ModelViz\backend\static\SpamTextCSV.csv')
df["clean_text"] = df["Message"].apply(clean_text)
label_encoder = LabelEncoder()
df["label"] = label_encoder.fit_transform(df["Category"])
vectorizer = TfidfVectorizer(max_features=5000)
X_train, X_test, y_train, y_test = train_test_split(df["clean_text"], df["label"], test_size=0.2, random_state=42)
X_train_tfidf = vectorizer.fit_transform(X_train).toarray()
X_test_tfidf = vectorizer.transform(X_test).toarray()

def train_nn(hidden_neurons, activation_function, epochs, learning_rate):
    
    model = Sequential([
        Dense(hidden_neurons, activation=activation_function, input_shape=(X_train_tfidf.shape[1],)),
        Dense(32, activation=activation_function),
        Dense(1, activation="sigmoid")  # Binary classification (Spam or Ham)
    ])
    model.compile(optimizer=Adam(learning_rate=learning_rate), loss="binary_crossentropy", metrics=["accuracy"])

    # Train the model
    history = model.fit(X_train_tfidf, y_train, epochs=epochs, validation_data=(X_test_tfidf, y_test), batch_size=32, verbose=1)
    final_accuracy = history.history["val_accuracy"][-1]
    return final_accuracy