import nltk
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import one_hot
import re
from nltk.corpus import stopwords
import joblib
from tensorflow.keras.models import load_model

model = load_model('./lstm_model.keras')

dependencies = joblib.load("lstm_dependencies.pkl")
vocab_size = dependencies["vocab_size"]
sentence_len = dependencies["sentence_len"]
def classify_message(message):
    #We will treat message as a paragraphs containing multiple sentences(lines)
    #we will extract individual lines
    for sentences in message:
        sentences=nltk.sent_tokenize(message)

        #Iterate over individual sentences
        for sentence in sentences:
            #replace all special characters
            words=re.sub("[^a-zA-Z]"," ",sentence)

            #perform word tokenization of all non-english-stopwords
            if words not in set(stopwords.words('english')):
                word=nltk.word_tokenize(words)
                word=" ".join(word)

    #perform one_hot on tokenized word
    oneHot=[one_hot(word,n=vocab_size)]

    #create an embedded documnet using pad_sequences
    #this can be fed to our model
    text=pad_sequences(oneHot,maxlen=sentence_len,padding="pre")
    #predict the text using model
    predict=model.predict(text)
    print(predict)
    #if predict value is greater than 0.5 its a spam
    if predict>0.5:
        return 1
    #else the message is not a spam
    else:
        return 0
