from sklearn.feature_extraction.text import TfidfVectorizer
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import joblib
import numpy as np
stemmer=PorterStemmer()
vectorizer = joblib.load(r'd:\ModelViz\backend\vectorizer.pkl')
def vectorize_text(preprocessed_text):
    # Initialize TfidfVectorizer

    # Fit and transform the preprocessed text
    vectorized_text = vectorizer.transform([preprocessed_text])

    # Return the vectorized representation
    return vectorized_text

def preprocess_text(text):
    # Remove non-alphabetical characters
    text = re.sub("[^a-zA-Z]", " ", text)
    text = text.lower()
    text = text.split()
    text = [stemmer.stem(word) for word in text if word not in set(stopwords.words("english"))]
    text = " ".join(text)
    return text

model = joblib.load('./svm_joblib.pkl')
def explain_prediction(message):
    # Preprocess the message (as done during training)
    message = re.sub("[^a-zA-Z]", " ", message)
    message = message.lower()
    message = [word for word in message.split() if word not in stopwords.words('english')]
    message = " ".join(message)
    
    # Vectorize the message
    vectorized_message = vectorizer.transform([message])
    
    # Get the coefficients for spam classification
    feature_names = vectorizer.get_feature_names_out()
    coefficients = model.coef_.toarray()[0]
    
    # Find contributing features
    word_importance = {}
    for idx, value in enumerate(vectorized_message.toarray()[0]):
        if value > 0:
            word_importance[feature_names[idx]] = coefficients[idx]

    # Sort words by importance
    sorted_words = sorted(word_importance.items(), key=lambda x: x[1], reverse=True)
    
    # Display the results
    # print("Message:", message)
    # print("Top contributing words for spam classification:")
    # for word, importance in sorted_words[:5]:  # Top 5 words
    #     print(f"{word}: {importance:.4f}")
    result = {
        "top_contributing_words": [
            {"word": word, "importance": importance} for word, importance in sorted_words[:5]  # Top 5 words
        ]
    }
    return result

# Example usage

    