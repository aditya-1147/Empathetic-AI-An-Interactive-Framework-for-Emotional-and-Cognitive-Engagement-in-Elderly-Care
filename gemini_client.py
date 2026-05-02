import os
from google import genai

from persona.persona_manager import load_persona, build_persona_prompt
from memory.memory_manager import retrieve_memories
from safety.safety_manager import (
    detect_emotional_dependency,
    get_self_disclosure_message,
    filter_ai_response
)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = "gemini-2.5-flash"

persona = load_persona()


def build_memory_context():
    """
    Retrieves recent memories and converts them into
    safe contextual hints for the LLM.
    """

    memories = retrieve_memories(limit=5)

    if not memories:
        return ""

    memory_lines = []

    for memory_type, content, image_path in memories:

        if image_path:
            memory_lines.append(
                f"- ({memory_type}) The user once shared an image described as: {content}"
            )
        else:
            memory_lines.append(
                f"- ({memory_type}) {content}"
            )

    return (
        "Context about the user (for gentle personalization only):\n"
        + "\n".join(memory_lines)
        + "\n\nRules:\n"
        "- Do not claim involvement in these memories\n"
        "- Mention only if relevant and comforting\n"
    )


def generate_response(user_message: str, emotion: str) -> dict:
    """
    Generates an emotionally adaptive, persona-consistent,
    memory-aware, and safety-filtered AI response.

    Returns:
        dict:
        {
            "text": AI response text,
            "emotion": detected emotion
        }
    """

    try:
        persona_prompt = build_persona_prompt(persona, emotion)

        memory_context = build_memory_context()

        full_prompt = f"""
{persona_prompt}

The user is currently feeling: {emotion}

{memory_context}

Global behavior rules:
- You are an AI companion, not a human
- Do not claim physical presence
- Do not present yourself as a replacement for real people
- Encourage autonomy and real-world connection
- Avoid clinical or medical authority
- Be warm, calm, respectful, and reassuring

User message:
{user_message}

Respond as the AI companion:
"""

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=[
                {
                    "role": "user",
                    "parts": [{"text": full_prompt}]
                }
            ]
        )

        ai_text = response.text.strip()


        ai_text = filter_ai_response(ai_text)

        if detect_emotional_dependency(user_message):
            ai_text += "\n\n" + get_self_disclosure_message()

        return {
            "text": ai_text,
            "emotion": emotion
        }

    except Exception as e:

        # Safe fallback response
        return {
            "text": "I'm here with you. Something went wrong on my side, but we can try again.",
            "emotion": "Calm"
        }