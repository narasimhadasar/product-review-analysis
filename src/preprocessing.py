# src/preprocessing.py
import re

def clean_text(text):
    if text is None:
        return ""
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    return text.strip()

def preprocess(df):
    required_cols = ["review_text"]
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")
    
    df = df.dropna(subset=["review_text"])
    df["clean_review"] = df["review_text"].apply(clean_text)
    return df
