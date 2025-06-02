# Emotion-Aware Chatbot for Mental Health Support

![Project Banner](https://via.placeholder.com/800x300?text=Emotion-Aware+Chatbot+for+Mental+Health+Support)

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
