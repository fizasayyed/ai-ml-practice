import pickle
import re

# Load the model (Change path accordingly)
model_path = '/home/GitHub/text_summarisation_trad_NLP/sentiment_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Load the CountVectorizer (BoW) > (Change path accordingly)
vectorizer_path = '/home/GitHub/text_summarisation_trad_NLP/vectorizer.pkl'
with open(vectorizer_path, 'rb') as file:
    vectorizer = pickle.load(file)

# Function to clean and preprocess the input text
def clean_text(text):
    text = text.lower()  # Lowercase the text
    text = re.sub(r'[^a-z\s]', '', text)  # Remove punctuation and numbers
    return text

# Take input from the user
user_input = input("Enter a sentence for sentiment analysis: ")

# Preprocess the input
cleaned_input = clean_text(user_input)

# Transform the input using the vectorizer
input_vector = vectorizer.transform([cleaned_input])  # again using the list to keep the format

# Make prediction
prediction = model.predict(input_vector)

# Print the prediction result
print(f"Predicted Sentiment: '{prediction[0]}'")
