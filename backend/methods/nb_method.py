import joblib
def predict_spam_nb(message):
  vectorizer = joblib.load('countVectorizer.pkl')
  model = joblib.load('./naivebayes_joblib.pkl')

  # Vectorize the message
  message_count = vectorizer.transform([message])  # Note: Input should be a list

  # Make the prediction
  prediction = model.predict(message_count)

  return prediction[0]