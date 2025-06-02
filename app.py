import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F
import asyncio

# Fix for asyncio event loop issues
try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# -------- Page Setup --------
st.set_page_config(page_title="Emotion Predictor", page_icon="💬", layout="centered")

# -------- Title --------
st.markdown("""
    <div style="text-align: center;">
        <h2 style="color: #4B8BBE;">💬 Emotion-Aware Chatbot</h2>
        <p style="font-size: 1.1rem;">Understand how you're feeling by analyzing your message</p>
    </div>
""", unsafe_allow_html=True)

# -------- Device Setup --------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# -------- Load Model & Tokenizer from Hugging Face --------
@st.cache_resource
def load_model():
    model_id = "HamzaNawaz17/TextEmotionDetectionModel"
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        model = AutoModelForSequenceClassification.from_pretrained(model_id)
        model.to(device)
        model.eval()
        return tokenizer, model
    except Exception as e:
        st.error(f"Model loading failed: {str(e)}")
        return None, None

tokenizer, model = load_model()

if tokenizer is None or model is None:
    st.stop()

# -------- Emotion Labels --------
emotion_labels = ['anger', 'fear', 'joy', 'love', 'sadness']

# -------- Prediction Function --------
def predict_emotion(text):
    try:
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
        inputs = {key: val.to(device) for key, val in inputs.items()}
        with torch.no_grad():
            outputs = model(**inputs)
            probs = F.softmax(outputs.logits, dim=1)
            predicted = torch.argmax(probs, dim=1).item()
            confidence = probs[0][predicted].item()
        return emotion_labels[predicted], confidence
    except Exception as e:
        st.error(f"Prediction error: {str(e)}")
        return None, None

# -------- Emotion-Based Responses --------
response_templates = {
    'anger': "It sounds like you're upset. I'm here to listen. 🧘",
    'fear': "It's okay to feel afraid. You're not alone. 🤝",
    'joy': "I'm so happy to hear that! 😊 Keep spreading the joy!",
    'love': "Love is such a beautiful emotion. Cherish it. 💖",
    'sadness': "I'm sorry you're feeling down. Things will get better. 🌧️☀️"
}

# -------- UI Elements --------
st.markdown("### How are you feeling today?")
user_input = st.text_area(
    "Enter your message:",
    height=140,
    placeholder="Type your thoughts here...",
    label_visibility="visible"
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    analyze_button = st.button("🔍 Analyze Emotion")

if analyze_button and user_input.strip():
    with st.spinner("Analyzing..."):
        emotion, confidence = predict_emotion(user_input)
        if emotion and confidence:
            st.success(f"**Emotion:** {emotion.capitalize()} ({confidence * 100:.2f}% confidence)")
            st.info(response_templates.get(emotion, "Thank you for sharing."))
elif analyze_button and not user_input.strip():
    st.warning("Please enter a message to analyze.")

# -------- Footer --------
st.markdown("""
    <hr style="margin-top: 2rem;">
    <div style='text-align: center; font-size: 0.9rem;'>
        Made with ❤️ using Hugging Face and Streamlit | Optimized for 🖥️ & 📱
    </div>
""", unsafe_allow_html=True)
