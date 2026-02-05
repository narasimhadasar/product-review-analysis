# src/affinity.py
def brand_category_affinity(reviews_df):
    required_cols = ["brand", "category", "sentiment_score"]
    missing_cols = [col for col in required_cols if col not in reviews_df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")
    
    affinity = (
        reviews_df.groupby(["brand", "category"])
        .agg(
            avg_sentiment=("sentiment_score", "mean"),
            review_count=("sentiment_score", "count")
        )
        .reset_index()
    )
    return affinity

