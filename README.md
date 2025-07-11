# Emotion-Aware Chatbot for Mental Health Support

---

## 🌟 Introduction

In today's digital age, many individuals lack immediate access to mental health support. Our Emotion-Aware Chatbot bridges this gap by analyzing textual input to detect emotional states and respond with empathy, offering preliminary mental well-being support.

---

## 🎯 Project Objectives

- Detect emotional states from text input with high accuracy
- Provide empathetic, context-aware responses
- Offer immediate mental health support
- Reduce barriers to accessing emotional support

---

## 🚀 Key Features

| Feature                    | Description                                         |
|----------------------------|-----------------------------------------------------|
| **Real-time Emotion Detection** | Identifies 5 core emotions: anger, fear, joy, love, sadness |
| **Contextual Responses**    | Delivers tailored empathetic responses for each emotion |
| **High Accuracy Model**     | 93.8% accurate emotion classification (F1-score: 0.938) |
| **Privacy-Focused**         | No data storage or logging of sensitive conversations |

---

## 📊 Model Performance

Our fine-tuned BERT model demonstrates exceptional performance:

| Metric        | Score    |
|---------------|----------|
| Accuracy      | 93.8%    |
| F1-Score      | 0.938    |
| Precision     | 0.938    |
| Recall        | 0.938    |
| Inference Speed | 179.84 samples/sec |

---

## 🔧 Architecture

```mermaid
graph TD
    A[User Input] --> B[Emotion Detection]
    B --> C{Emotion Class}
    C -->|anger| D[Empathetic Response]
    C -->|fear| E[Supportive Response]
    C -->|joy| F[Positive Reinforcement]
    C -->|love| G[Affirming Response]
    C -->|sadness| H[Comforting Response]
```
## 🧰 Technology Stack
- Natural Language Processing: Hugging Face Transformers
- Machine Learning Framework: PyTorch
- Web Interface: Streamlit

*Model: Fine-tuned BERT (base-uncased)*

🏁 Getting Started
✅ Prerequisites
Python 3.8+

### pip package manager

#### 💻 Installation
```bash 
git clone https://github.com/your-repo/emotion-chatbot.git
cd emotion-chatbot
pip install -r requirements.txt
```
#### ▶️ Running the Application
```bash 
streamlit run app.py
``` 
## 📂 Project Structure
```plaintext
emotion-chatbot/
├── app.py              # Main application file
├── requirements.txt    # Dependency list
├── README.md           # This documentation
└── assets/             # Additional resources
```

### 🌈 Emotion Support Matrix
|Emotion    |Example Input	                        |Bot Response                                                     |
|-----------|---------------------------------------|-----------------------------------------------------------------|
|Anger	    |"I'm so frustrated with everything!"	|It sounds like you're upset. I'm here to listen. 🧘"             |
|Fear	    |"I'm scared about what might happen"	|"It's okay to feel afraid. You're not alone. 🤝"                 |
|Joy	    |"I got the promotion!"    	            |"I'm so happy to hear that! 😊 Keep spreading the joy!"          |
|Love	    |"I cherish my partner so much"	        |"Love is such a beautiful emotion. Cherish it. 💖"               |
|Sadness	|"I've been feeling really down"    	|"I'm sorry you're feeling down. Things will get better. 🌧️☀️"    |

📜 License
This project is licensed under the MIT License – see the LICENSE file for details.

📧 Contact
For inquiries, please contact: iamhamzanawaz14@gmail.com

⚠️ Disclaimer: This chatbot is not a substitute for professional mental health care. If you're experiencing severe distress, please contact a licensed professional.
