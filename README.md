# 🤖 Empathetic AI Companion with Real-Time Avatar Generation

<p align="center">
  <b>An Emotion-Aware Conversational AI with Talking Avatar</b><br>
  Bridging Human Emotions and Artificial Intelligence
</p>

<p align="center">
  <img src="https://img.shields.io/badge/AI-Emotion%20Aware-blue" />
  <img src="https://img.shields.io/badge/LLM-Integrated-green" />
  <img src="https://img.shields.io/badge/Avatar-SadTalker-orange" />
  <img src="https://img.shields.io/badge/Status-Completed-success" />
</p>

---

## 📌 Overview

This project presents an **Emotionally Intelligent AI System** capable of:

- Understanding user emotions  
- Generating empathetic responses  
- Converting responses into speech  
- Rendering a **realistic talking avatar with expressions**  

It simulates **human-like interaction**, making it useful for mental health support, virtual assistants, and human-computer interaction systems.

---

## 🎯 Key Highlights

✔ Emotion Detection in ~1 second  
✔ AI Response Generation in ~2 seconds  
✔ Talking Avatar Generation (~20 seconds)  
✔ End-to-End Emotion-Aware Pipeline  
✔ Real-Time Interaction via Streamlit UI  

---

## 🚀 Features

- 🎭 **Emotion Detection**
  - Detects: *Happy, Sad, Angry, Neutral*
  - Fast and efficient inference

- 💬 **Empathetic Response Generation**
  - Context-aware replies using LLMs
  - Emotion-conditioned outputs

- 🔊 **Text-to-Speech (TTS)**
  - Converts AI responses into natural speech

- 🧑‍🎤 **Talking Avatar Generation**
  - Lip-sync + facial animation using SadTalker
  - Emotion-driven expressions

- 🌐 **Interactive UI**
  - Built with Streamlit
  - Smooth user experience

---

## 🏗️ System Architecture

```
User Input (Text/Image)
        ↓
Emotion Detection Model
        ↓
Emotion Label
        ↓
LLM Response Generator
        ↓
Text Response
        ↓
Text-to-Speech (TTS)
        ↓
Audio Output
        ↓
SadTalker Avatar Generation
        ↓
Talking Avatar Video
```

---

## 🧠 Tech Stack

### 🔹 AI / Machine Learning
- Python  
- PyTorch  
- HuggingFace Transformers  
- OpenAI / LLM APIs  

### 🔹 Computer Vision & Audio
- OpenCV  
- Emotion Recognition Models  
- TTS (gTTS / Coqui)  

### 🔹 Avatar Generation
- SadTalker  

### 🔹 Backend & Deployment
- Streamlit (Frontend)  
- Flask / FastAPI  
- Google Colab GPU + ngrok  

---

## 📂 Project Structure

```
Empathetic-AI-Companion/

├── app.py                  # Streamlit frontend
├── server.py               # Backend (Colab GPU + ngrok)
├── requirements.txt

├── emotion/
│   ├── emotion_model.py
│   └── utils.py

├── llm/
│   └── response_generator.py

├── tts/
│   └── tts_engine.py

├── avatar/
│   ├── sadtalker_inference.py
│   └── configs/

├── assets/
│   ├── images/
│   └── audio/

├── outputs/
│   └── videos/

└── README.md
```

---

## 📊 Performance Metrics

| Module                  | Time |
|------------------------|------|
| Emotion Detection      | ~1 sec |
| Response Generation    | ~2 sec |
| Avatar Generation      | ~80 sec |

---

## 🧪 End-to-End Workflow

1. User inputs text or image  
2. Emotion is detected  
3. AI generates empathetic reply  
4. Reply converted into speech  
5. Avatar lip-syncs and expresses emotion  

---

## 🔮 Future Enhancements

- ⚡ Real-time avatar generation (low latency)
- 🎙 Voice input support
- 🌍 Multilingual interaction
- 🧍 Full-body expressive avatars
- 🧠 Fine-tuned emotion-aware LLM

---

## 💡 Applications

- Mental Health Support Systems  
- Virtual Assistants  
- AI Companions  
- Customer Interaction Systems  
- Educational Tools  

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository  
2. Create a new branch  
3. Commit changes  
4. Submit a pull request  

---

## 👨‍💻 Author

**Aditya Goel**  
Capstone Project – Empathetic AI Companion  

---

## ⭐ Show Your Support

If you found this project useful, please ⭐ the repo!
