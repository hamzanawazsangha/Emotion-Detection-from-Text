# app.py
import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch

# Set page layout
st.set_page_config(page_title="Emotion Detection", layout="centered")

# Sidebar info
with st.sidebar:
    st.header("📘 Model Info")
    st.markdown("""
    - **Model:** `HamzaNawaz17/TextEmotionDetectionModel`
    - **Base:** BERT-based Transformer
    - **Trained for:** Text Emotion Classification
    - **Accuracy:** ~94%
    """)
    st.markdown("---")
    st.write("Created with ❤️ using Hugging Face and Streamlit")

# Main title
st.title("😊 Emotion Detection from Text")
st.subheader("Let AI detect how you're feeling!")

# Text input with placeholder
user_input = st.text_area(
    "Your Message ✍️", 
    placeholder="e.g., I'm feeling really excited about my day!",
    label_visibility="visible"
)

# Load model only once
@st.cache_resource
def load_pipeline():
    tokenizer = AutoTokenizer.from_pretrained("HamzaNawaz17/TextEmotionDetectionModel")
    model = AutoModelForSequenceClassification.from_pretrained("HamzaNawaz17/TextEmotionDetectionModel")
    return pipeline("text-classification", model=model, tokenizer=tokenizer)

# Emoji mapping
EMOJI_MAP = {
    "joy": "😄",
    "sadness": "😢",
    "anger": "😠",
    "fear": "😨",
    "love": "❤️",
    "surprise": "😲",
    "neutral": "😐"
}

# Predict button
if user_input:
    with st.spinner("Analyzing your emotion..."):
        classifier = load_pipeline()
        result = classifier(user_input)[0]
        label = result['label'].lower()
        emoji = EMOJI_MAP.get(label, "🔍")
        score = result['score']
        st.markdown(f"### {emoji} **{label.capitalize()}**  \nConfidence: `{score:.2f}`")

# Footer
st.markdown("---")
st.caption("Powered by 🤗 Hugging Face | Deployed on 🌐 Streamlit Cloud")
