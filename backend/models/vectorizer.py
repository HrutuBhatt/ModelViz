from sklearn.feature_extraction.text import TfidfVectorizer
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import joblib
stemmer=PorterStemmer()
def vectorize_text(preprocessed_text):
    # Initialize TfidfVectorizer
    vectorizer = joblib.load(r'd:\ModelViz\backend\vectorizer.pkl')

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