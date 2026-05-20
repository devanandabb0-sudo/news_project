POSITIVE_WORDS = [
    "good", "great", "excellent", "positive",
    "growth", "success", "profit", "happy"
]

NEGATIVE_WORDS = [
    "bad", "poor", "negative", "loss",
    "failure", "drop", "crash", "sad"
]


def analyze_sentiment(text):

    text = text.lower()

    positive_score = sum(
        word in text for word in POSITIVE_WORDS
    )

    negative_score = sum(
        word in text for word in NEGATIVE_WORDS
    )

    score = positive_score - negative_score

    if score > 0:
        sentiment = "Positive"
    elif score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, score