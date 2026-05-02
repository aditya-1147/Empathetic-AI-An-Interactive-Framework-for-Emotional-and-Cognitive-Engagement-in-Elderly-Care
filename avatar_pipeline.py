from avatar.tts_engine import generate_speech
from avatar.colab_sadtalker_client import generate_avatar


def generate_avatar_response(ai_text: str, face_image_path: str) -> str:
    """
    Full avatar pipeline:
    AI text → speech → SadTalker GPU → video
    """

    audio_path = generate_speech(ai_text)

    # Generate avatar video
    video_path = generate_avatar(audio_path, face_image_path)

    return video_path