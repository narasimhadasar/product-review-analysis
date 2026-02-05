# src/sentiment.py
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def get_sentiment_label(score):
    if score > 0.05:
        return "positive"
    elif score < -0.05:
        return "negative"
    else:
        return "neutral"

def analyze_sentiment(df):
    required_cols = ["clean_review"]
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")
    
    df["clean_review"] = df["clean_review"].fillna("")
    scores = df["clean_review"].apply(lambda x: analyzer.polarity_scores(x)["compound"])
    df["sentiment_score"] = scores
    df["sentiment_label"] = df["sentiment_score"].apply(get_sentiment_label)
    return df
