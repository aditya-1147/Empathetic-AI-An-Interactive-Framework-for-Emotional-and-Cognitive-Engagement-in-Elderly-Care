🤖 Empathetic AI Companion with Real-Time Avatar Generation
An intelligent AI system that detects human emotions and responds empathetically through both text and dynamically generated talking avatars. This project integrates emotion recognition, natural language processing, and AI-driven avatar animation to create a human-like conversational experience.
📌 Overview
This project aims to bridge the gap between humans and machines by enabling emotionally aware interactions. The system:
Detects user emotions from input (text/image)
Generates context-aware empathetic responses
Converts responses into speech
Animates a realistic talking avatar in real-time
🚀 Features
🎭 Emotion Detection
Detects emotions like happy, sad, angry, neutral
Fast inference (~1 sec)
💬 Empathetic Response Generation
Context-aware AI responses using LLMs
Emotion-conditioned replies
🔊 Text-to-Speech (TTS)
Converts responses into natural speech
🧑‍🎤 AI Avatar Generation
Talking avatars using SadTalker
Emotion-driven facial expressions
📊 Performance Optimized
Response generation: ~2 sec
Avatar generation: ~20 sec
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

🧠 Technologies Used
🔹 AI / ML
Python
PyTorch
Transformers (HuggingFace)
OpenAI / LLM APIs
🔹 Computer Vision & Audio
OpenCV
Emotion Detection Models
TTS Engines (gTTS / Coqui / etc.)
🔹 Avatar Generation
SadTalker (for lip-sync + animation)
🔹 Backend & Deployment
Streamlit (UI)
Flask / FastAPI (backend)
Google Colab GPU (via ngrok)
📂 Project Structure
Empathetic-AI-Companion/
│
├── app.py                  # Streamlit frontend
├── server.py              # Backend (Colab GPU + ngrok)
├── requirements.txt
│
├── emotion/
│   ├── emotion_model.py
│   └── utils.py
│
├── llm/
│   ├── response_generator.py
│
├── tts/
│   ├── tts_engine.py
│
├── avatar/
│   ├── sadtalker_inference.py
│   └── configs/
│
├── assets/
│   ├── images/
│   └── audio/
│
├── outputs/
│   ├── videos/
│
└── README.md
📊 Performance Metrics
Module	Time Taken
Emotion Detection	~1 sec
Response Generation	~2 sec
Avatar Generation	~20 sec
🧪 Sample Workflow
User inputs text or image
System detects emotion
AI generates empathetic reply
Reply converted to speech
Avatar lip-syncs and expresses emotion
