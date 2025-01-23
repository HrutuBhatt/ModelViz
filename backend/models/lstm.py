import joblib
import pandas as pd
import io

df = pd.read_csv(r'd:\ModelViz\backend\static\SpamTextCSV.csv') 
print(df.head())

import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline



#extra column indicating length of message
df["Message Length"]=df["Message"].apply(len)

#figure
# fig=plt.figure(figsize=(10,6))
# sns.histplot(
#     x=df["Message Length"],
#     hue=df["Category"]
# )
# plt.title("ham & spam messege length comparision")
# plt.show()

# ham_desc = df[df["Category"]=="ham"]["Message Length"].describe()
# spam_desc = df[df["Category"]=="spam"]["Message Length"].describe()
# print("Ham Message Length Stats")
# print(ham_desc)
# print("Spam Message Length Stats")
# print(spam_desc)

# df["Category"].value_counts()
# sns.countplot(
#     data=df,
#     x="Category"
# )
# plt.title("ham vs spam")
# plt.show()

ham_count=df["Category"].value_counts()[0]
spam_count=df["Category"].value_counts()[1]

total_count=df.shape[0]

# print("Ham contains:{:.2f}% of total data.".format(ham_count/total_count*100))
# print("Spam contains:{:.2f}% of total data.".format(spam_count/total_count*100))

"""undersampling , due to imbalanced dataset"""

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

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import one_hot
vocab_size=10000
# The one_hot function converts the word into a numerical
# vector representation. In one-hot encoding, each word is
# represented by a vector of size vocab_size, where all
# elements are 0 except for the element corresponding to the
# word's index in the vocabulary, which is set to 1.
oneHot_doc=[one_hot(words,n=vocab_size)
           for words in corpus
           ]

data["Message Length"].describe()

# fig=plt.figure(figsize=(12,8))
# sns.kdeplot(
#     x=data["Message Length"],
#     hue=data["Category"]
# )
# plt.title("ham & spam messege length comparision")
# plt.show()

# from keras import pad_sequences
from tensorflow.keras.preprocessing.sequence import pad_sequences
sentence_len=200
embedded_doc=pad_sequences(
    oneHot_doc,
    maxlen=sentence_len,
    padding="pre"
)

data["Label"]=data["Category"].map(
    {
        "ham":0,
        "spam":1
    }
)

extract_features=pd.DataFrame(
    data=embedded_doc
)
target=data["Label"]

data.head()

df_final=pd.concat([extract_features,target],axis=1)
df_final.head()

"""above numbers are indices of words in vocab"""

X=df_final.drop("Label",axis=1)
y=df_final["Label"]

from sklearn.model_selection import train_test_split
X_trainval, X_test, y_trainval, y_test = train_test_split(
    X,
    y,
    random_state=42,
    test_size=0.15
)

#trainval: training and validation (85%) and testing (15%)

#85% training and 15% validation from above split
X_train,X_val,y_train,y_val=train_test_split(
    X_trainval,
    y_trainval,
    random_state=42,
    test_size=0.15
)

from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Embedding
from tensorflow.keras.models import Sequential
model=Sequential()

feature_num=100
model.add(
    Embedding(
        input_dim=vocab_size,
        output_dim=feature_num,
        input_length=sentence_len
    )
)
model.add(
    LSTM(
    units=128
    )
)

model.add(
    Dense(
        units=1,
        activation="sigmoid"
    )
)


from tensorflow.keras.optimizers import Adam
model.compile(
    optimizer=Adam(
    learning_rate=0.001
    ),
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.fit(
    X_train,
    y_train,
    validation_data=(
        X_val,
        y_val
    ),
    epochs=10
)

y_pred=model.predict(X_test)
y_pred=(y_pred>0.5)

# joblib.dump(model, 'lstm_joblib.pkl')
#save model 
# model.save('lstm_model.keras')  
from sklearn.metrics import accuracy_score,confusion_matrix, recall_score, precision_score, f1_score
score=accuracy_score(y_test,y_pred)
precision=precision_score(y_test,y_pred)
recall=recall_score(y_test,y_pred)
f1=f1_score(y_test,y_pred)
print("Accuracy Score:{:.2f}%".format(score*100))
print("Precision Score:{:.2f}%".format(precision*100))
print("Recall Score:{:.2f}%".format(recall*100))
print("F1 Score:{:.2f}%".format(f1*100))

metrics_lstm = {
    "accuracy": score,
    "precision": precision,
    "recall": recall,
    "f1" : f1
}

# Save dependencies
# joblib.dump(metrics_lstm, "metrics_lstm.pkl")

cm=confusion_matrix(y_test,y_pred)
fig=plt.figure(figsize=(12,8))
sns.heatmap(
    cm,
    annot=True,
)
plt.title("Confusion Matrix")
cm

# The function take model and message as parameter
def classify_message(model,message):

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

    #create an embedded document using pad_sequences
    #this can be fed to our model
    text=pad_sequences(oneHot,maxlen=sentence_len,padding="pre")
    #predict the text using model
    predict=model.predict(text)

    #if predict value is greater than 0.5 its a spam
    if predict>0.5:
        print("It is a spam")
    #else the message is not a spam
    else:
        print("It is not a spam")


message1="I am having a bad day and I would like to have a break today"
message2="Scam Alert! 3000$ debited from your account. click link to find out"

classify_message(model,message2)
# dependencies = {
#     "vocab_size": vocab_size,
#     "sentence_len": sentence_len,
# }

# Save dependencies
# joblib.dump(dependencies, "lstm_dependencies.pkl")


