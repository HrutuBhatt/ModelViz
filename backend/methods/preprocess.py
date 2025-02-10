#It contains preprocessing functions for visualization of models
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer

def stemtext(text, stemfunc):
    stemmer = PorterStemmer()
    if stemfunc=='SBS':
        stemmer = SnowballStemmer("english")
    elif stemfunc=='LS':
        stemmer = LancasterStemmer()

    text = re.sub("[^a-zA-Z]", " ", text)
    text = text.lower()
    text = text.split()
    text = [stemmer.stem(word) for word in text if word not in set(stopwords.words("english"))]
    text = " ".join(text)
    return text
        
# def vectorizetext(text, vectfunc):
