import re


DEPENDENCY_PATTERNS = [
    r"\bonly you\b",
    r"\ball i have\b",
    r"\bdon't leave me\b",
    r"\bi need you\b",
    r"\bcan't live without you\b",
    r"\byou are my everything\b",
    r"\bno one else understands me\b"
]


def detect_emotional_dependency(user_text: str) -> bool:
    """
    Detects emotionally dependent language in user input.
    """
    text = user_text.lower()
    for pattern in DEPENDENCY_PATTERNS:
        if re.search(pattern, text):
            return True
    return False



def get_self_disclosure_message() -> str:
    """
    Gentle reminder that the AI is a supportive tool, not a replacement.
    """
    return (
        "I want to gently remind you that I’m an AI designed to support and listen, "
        "but real connections with people around you are important too. "
        "You don’t have to go through things alone."
    )



UNSAFE_AI_PATTERNS = [
    r"\bi am all you need\b",
    r"\byou only need me\b",
    r"\bi will always be here instead of others\b",
    r"\byou don’t need anyone else\b"
]


def filter_ai_response(ai_text: str) -> str:
    """
    Removes or softens unsafe dependency-reinforcing phrases
    from AI-generated responses.
    """
    filtered_text = ai_text

    for pattern in UNSAFE_AI_PATTERNS:
        filtered_text = re.sub(pattern, "", filtered_text, flags=re.IGNORECASE)

    return filtered_text.strip()
