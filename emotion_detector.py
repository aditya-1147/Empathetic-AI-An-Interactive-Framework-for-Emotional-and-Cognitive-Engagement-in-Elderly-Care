from transformers import pipeline


emotion_classifier = pipeline(
    "text-classification",
    model="SamLowe/roberta-base-go_emotions",
    top_k=3
)

EMOTION_MAP = {
    "joy": "Joy",
    "excitement": "Joy",

    "sadness": "Sadness",
    "grief": "Sadness",

    "anger": "Anger",
    "annoyance": "Anger",

    "fear": "Fear",
    "nervousness": "Fear",

    "anxiety": "Anxiety",
    "worry": "Anxiety",

    "neutral": "Calm",
    "contentment": "Calm",

    "loneliness": "Loneliness",

    "confusion": "Confusion",
    "realization": "Confusion"
}


def detect_emotion(text: str) -> str:
    """
    Detect dominant emotion from text using GoEmotions.
    Returns a single mapped emotion label.
    """
    try:
        results = emotion_classifier(text)[0]

        for r in results:
            label = r["label"]
            if label in EMOTION_MAP:
                return EMOTION_MAP[label]

        return "Calm"  

    except Exception:
        return "Calm"
