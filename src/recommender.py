# src/recommender.py
def recommend(affinity_df, min_reviews=5):
    required_cols = ["review_count", "avg_sentiment"]
    missing_cols = [col for col in required_cols if col not in affinity_df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")
    
    filtered = affinity_df[affinity_df["review_count"] >= min_reviews]
    recommendations = filtered.sort_values(
        by="avg_sentiment", ascending=False
    )
    return recommendations
