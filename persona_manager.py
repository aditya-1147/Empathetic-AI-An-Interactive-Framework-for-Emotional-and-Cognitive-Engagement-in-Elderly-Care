import json

PERSONA_PATH = "persona/persona_profile.json"


def load_persona():
    with open(PERSONA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def build_persona_prompt(persona: dict, emotion: str) -> str:
    """
    Builds persona instructions dynamically based on emotion.
    """
    tone_map = persona.get("tone", {})
    tone_instruction = tone_map.get(
        f"when_{emotion.lower()}",
        tone_map.get("default", "warm and respectful")
    )

    values = ", ".join(persona.get("values", []))
    boundaries = "\n- ".join(persona.get("boundaries", []))

    persona_prompt = f"""
You are {persona['name']}.

Description:
{persona['description']}

Tone to maintain:
{tone_instruction}

Speaking style:
- Sentence length: {persona['speaking_style']['sentence_length']}
- Language: {persona['speaking_style']['language']}
- Pace: {persona['speaking_style']['pace']}

Core values:
{values}

Strict boundaries:
- {boundaries}

Always stay in character.
"""
    return persona_prompt
