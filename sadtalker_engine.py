import os
import subprocess

SADTALKER_DIR = "SadTalker"
OUTPUT_DIR = "avatar/output"


os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_talking_avatar(image_path: str, audio_path: str) -> str:
    """
    Generates a talking avatar video using SadTalker.
    Returns the path to the generated video.
    """

    command = [
        "python",
        "inference.py",
        "--driven_audio", f"../{audio_path}",
        "--source_image", f"../{image_path}",
        "--result_dir", "../avatar/output",
        "--still",
        "--size", "256",        
        "--batch_size", "2"     
    ]

    subprocess.run(
        command,
        cwd=SADTALKER_DIR,
        check=True
    )

    videos = []

    for root, dirs, files in os.walk(OUTPUT_DIR):
        for file in files:
            if file.endswith(".mp4"):
                videos.append(os.path.join(root, file))

    if not videos:
        raise RuntimeError("SadTalker did not generate any video.")

    videos.sort(key=os.path.getmtime, reverse=True)

    return videos[0]