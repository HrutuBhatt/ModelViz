import pandas as pd
import io
import joblib
df = pd.read_csv(r'd:\ModelViz\backend\static\SpamTextCSV.csv')
# print(df.head())

"""Undersampling"""

import numpy as np
#compute the length of majority & minority class
minority_len=len(df[df["Category"]=="spam"])
majority_len=len(df[df["Category"]=="ham"])

#store the indices of majority and minority class
minority_indices=df[df["Category"]=="spam"].index
majority_indices=df[df["Category"]=="ham"].index

#generate new majority indices from the total majority_indices
#with size equal to minority class length so we obtain equivalent number of indices length
random_majority_indices=np.random.choice(
    majority_indices,
    size=minority_len,
    replace=False
)
#concatenate the two indices to obtain indices of new dataframe
undersampled_indices=np.concatenate([minority_indices,random_majority_indices])

# print(undersampled_indices)
#create df using new indices
data=df.loc[undersampled_indices]

#shuffle the sample
data=data.sample(frac=1)

#reset the index as its all mixed
data=data.reset_index()

#drop the older index
data=data.drop(
    columns=["index"],
)

data["Label"]=data["Category"].map(
    {
        "ham":0,
        "spam":1
    }
)

data.shape
data["Category"].value_counts()

# nltk.download('stopwords')
# nltk.download('punkt_tab')

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stemmer=PorterStemmer()
#declare empty list to store tokenized message
corpus=[]

#iterate through the data["Message"]
for message in data["Message"]:

    #replace every special characters, numbers etc.. with whitespace of message
    #It will help retain only letter/alphabets
    message=re.sub("[^a-zA-Z]"," ",message)

    #convert every letters to its lowercase
    message=message.lower()

    #split the word into individual word list
    message=message.split()

    #perform stemming using PorterStemmer for all non-english-stopwords
    message=[stemmer.stem(words)
            for words in message
             if words not in set(stopwords.words("english"))
            ]
    #join the word lists with the whitespace
    message=" ".join(message)

    #append the message in corpus list
    corpus.append(message)

corpus[0]

newdf = pd.DataFrame({"Message":corpus,"Label":data["Label"]})

newdf.head()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(corpus, newdf['Label'], test_size=0.15, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

joblib.dump(vectorizer, 'vectorizer.pkl')

from sklearn.svm import SVC

svm_model = SVC(kernel='linear')
svm_model.fit(X_train_vec, y_train)

# from sklearn.metrics import accuracy_score

# y_pred = svm_model.predict(X_test_vec)
# accuracy = accuracy_score(y_test, y_pred)
# print("Accuracy:", accuracy)

# prompt: give confusion matrix for above

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming y_test and y_pred are already defined from your previous code

# cm = confusion_matrix(y_test, y_pred)

# plt.figure(figsize=(8, 6))
# sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
#             xticklabels=['Ham', 'Spam'], yticklabels=['Ham', 'Spam'])
# plt.xlabel('Predicted')
# plt.ylabel('Actual')
# plt.title('Confusion Matrix')
# plt.show()

# prompt: construct a function that takes the model and sentence and prints whether sentence is spam or not spam

def predict_spam(model, sentence):
    # Preprocess the input sentence
    stemmer = PorterStemmer()
    sentence = re.sub("[^a-zA-Z]", " ", sentence)
    sentence = sentence.lower()
    sentence = sentence.split()
    sentence = [stemmer.stem(word) for word in sentence if word not in set(stopwords.words("english"))]
    sentence = " ".join(sentence)

    # Vectorize the sentence
    vectorized_sentence = vectorizer.transform([sentence])

    # Make the prediction
    prediction = model.predict(vectorized_sentence)[0]

    # Print the result
    if prediction == 1:
        print("Spam")
    else:
        print("Not Spam")

# prompt: call predict_spam by giving it a spam text


# import pickle
# with open('svm_pickle','wb') as f:
#     pickle.dump(svm_model,f)

# with open('svm_pickle','rb') as f:
#     mp = pickle.load(f)

# predict_spam(mp, "Going for shopping to buy dress")

joblib.dump(svm_model, 'svm_joblib.pkl')