import requests
import os
import time
import subprocess

COLAB_API = "https://erlinda-unexaminable-sororally.ngrok-free.dev/generate_avatar"


def convert_video_for_streamlit(input_path):
    """
    Convert video to browser-compatible format (CRITICAL FIX)
    """
    output_path = input_path.replace(".mp4", "_streamlit.mp4")

    command = [
        "ffmpeg",
        "-y",
        "-i", input_path,
        "-vcodec", "libx264",
        "-profile:v", "baseline",
        "-level", "3.0",
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        "-acodec", "aac",
        output_path
    ]

    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return output_path


def generate_avatar(audio_path, image_path):
    """
    Sends audio + image to Colab SadTalker API
    and saves + converts the returned video locally.
    """

    try:
        with open(audio_path, "rb") as audio_file, open(image_path, "rb") as image_file:

            files = {
                "audio": audio_file,
                "image": image_file
            }

            response = requests.post(
                COLAB_API,
                files=files,
                timeout=300
            )

        if response.status_code != 200:
            raise Exception(f"API Error: {response.status_code} - {response.text}")

        os.makedirs("avatar/output", exist_ok=True)

        raw_path = f"avatar/output/avatar_{int(time.time())}.mp4"

        with open(raw_path, "wb") as f:
            f.write(response.content)

        print("✅ Raw video saved:", raw_path)
        print("📦 Size:", os.path.getsize(raw_path))

        final_path = convert_video_for_streamlit(raw_path)

        print("🎥 Converted video:", final_path)

        return final_path

    except Exception as e:
        print("❌ Error in generate_avatar:", str(e))
        raise