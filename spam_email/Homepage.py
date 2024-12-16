import streamlit as st

st.title("Spam Email Detector")
st.markdown("""
### Introduction
Welcome to the **Spam Email Detector**! This application leverages a pre-trained machine learning model to classify emails as either "Spam" or "Not Spam".

### How It Works
- **Input**: You provide the text of an email that you want to classify.
- **Processing**: The application uses a state-of-the-art natural language processing (NLP) model to analyze the email content.
- **Output**: The model predicts whether the email is spam or not, helping you filter out unwanted or potentially harmful messages.

### Key Features
- **Accurate Detection**: The underlying model is trained on a large dataset of emails to ensure high accuracy.
- **Easy to Use**: Simply paste your email text into the input box, and the application will handle the rest.
- **Fast Processing**: Get results in real-time, thanks to the efficient model architecture.

### Usage
To use the Spam Email Detector, follow these simple steps:
1. Copy the text of the email you want to check.
2. Paste it into the input box provided.
3. Click on the "Analyze" button.
4. View the prediction to see if the email is classified as "Spam" or "Not Spam".

We hope this tool helps you keep your inbox clean and secure!
""")
