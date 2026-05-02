import os
from TTS.api import TTS

tts_model = TTS(model_name="tts_models/en/vctk/vits", progress_bar=False)

OUTPUT_DIR = "avatar/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_speech(text: str) -> str:
    output_path = os.path.join(OUTPUT_DIR, "speech.wav")

    tts_model.tts_to_file(
        text=text,
        speaker="p225",  
        file_path=output_path
    )

    return output_path