import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
st.set_page_config(page_title="SPAM EMAIL", page_icon="✉️", layout="wide")
st.header("🕵️ SPAM EMAIL")

def model(mail):
    
    model_path = ""
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)

# Example input
    email_text = mail
    inputs = tokenizer(email_text, return_tensors="pt", padding="max_length", truncation=True, max_length=128)

# Make prediction
    model.eval()
    with torch.no_grad():
        outputs = model(**inputs)

    predicted_label_id = torch.argmax(outputs.logits, dim=1).item()
    label_mapping = {0: "Not Spam", 1: "Spam"}
    predicted_label = label_mapping[predicted_label_id]

    return predicted_label

def main():
    if mail:= st.text_input("Enter the recevied email"):
        result = model(mail)
        if result == "Spam":
            st.error("# The email is spam")
        else:
            st.success("# The email is not spam")

if __name__ == "__main__":
    main()

