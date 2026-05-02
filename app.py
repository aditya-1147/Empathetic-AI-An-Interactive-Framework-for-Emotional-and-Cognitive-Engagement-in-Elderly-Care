import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import streamlit as st
import time

from ui.ui_components import display_header, user_input_box, send_button
from utils.config import APP_TITLE, APP_SUBTITLE

from llm.gemini_client import generate_response
from emotion.emotion_detector import detect_emotion

from memory.memory_manager import (
    init_db,
    store_image_memory
)

from avatar.avatar_pipeline import generate_avatar_response


def wait_for_file(file_path, timeout=20):
    start_time = time.time()

    while True:
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            return True

        if time.time() - start_time > timeout:
            return False

        time.sleep(0.5)


st.set_page_config(
    page_title=APP_TITLE,
    layout="centered"
)

display_header(APP_TITLE, APP_SUBTITLE)

st.caption("⚠️ AI-generated avatar responses. Use face images only with consent.")

init_db()


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "last_video" not in st.session_state:
    st.session_state.last_video = None


with st.expander("🖼️ Save a Memory (Optional)"):

    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    image_description = st.text_area("Describe this memory (optional)")

    memory_type = st.selectbox(
        "Memory category",
        ["scenery", "family_moment", "togetherness", "travel_place", "meaningful_object"]
    )

    if st.button("Save Memory"):

        if uploaded_image:
            os.makedirs("memory/images", exist_ok=True)

            image_path = f"memory/images/{uploaded_image.name}"

            with open(image_path, "wb") as f:
                f.write(uploaded_image.getbuffer())

            store_image_memory(memory_type, image_description, image_path)

            st.success("Memory saved successfully.")


st.subheader("Avatar Settings")

uploaded_face = st.file_uploader(
    "Upload a face image for avatar (optional)",
    type=["jpg", "png", "jpeg"]
)


for speaker, message in st.session_state.chat_history:
    if speaker == "user":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**AI:** {message}")



user_message = user_input_box()



if send_button():

    if user_message.strip():

        st.session_state.chat_history.append(("user", user_message))

        detected_emotion = detect_emotion(user_message)

        result = generate_response(user_message, detected_emotion)
        ai_text = result["text"]

        st.session_state.chat_history.append(("ai", ai_text))

        st.markdown(f"**AI:** {ai_text}")


        if uploaded_face:

            os.makedirs("avatar/output", exist_ok=True)

            face_path = "avatar/output/face.jpg"

            with open(face_path, "wb") as f:
                f.write(uploaded_face.getbuffer())

            
            progress_bar = st.progress(0)
            status_text = st.empty()

            try:
                
                status_text.text("🧠 Understanding emotion...")
                progress_bar.progress(10)
                time.sleep(0.5)

                
                status_text.text("💬 Generating AI response...")
                progress_bar.progress(20)
                time.sleep(0.5)

                
                status_text.text("🎤 Converting text to speech...")
                progress_bar.progress(35)
                time.sleep(0.5)

                
                status_text.text("☁️ Sending data to GPU server...")
                progress_bar.progress(50)

                
                video_path = generate_avatar_response(ai_text, face_path)

                
                status_text.text("🎭 Generating avatar animation...")
                progress_bar.progress(75)

                video_path = os.path.abspath(video_path)

                
                status_text.text("📦 Finalizing video...")
                progress_bar.progress(90)

                ready = wait_for_file(video_path)

                if ready:
                    progress_bar.progress(100)
                    status_text.text("✅ Avatar ready!")

                    st.session_state.last_video = video_path

                else:
                    st.error("❌ Video not ready.")

            except Exception as e:
                st.error("Avatar generation failed.")
                print(e)


if st.session_state.last_video:

    st.subheader("AI Avatar Response")

    video_path = st.session_state.last_video

    if os.path.exists(video_path):

        st.write("📂 Path:", video_path)
        st.write("📦 Size:", os.path.getsize(video_path))

        st.video(video_path, format="video/mp4")

    else:
        st.error("❌ Video file missing.")