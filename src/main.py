# src/main.py
import logging
import os
from data_loader import load_data
from data_mapper import map_columns
from preprocessing import preprocess
from sentiment import analyze_sentiment
from affinity import brand_category_affinity
from recommender import recommend

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    try:
        df = load_data("data/GrammarandProductReviews.csv")
        df = map_columns(df)
        df = preprocess(df)
        df = analyze_sentiment(df)

        affinity = brand_category_affinity(df)
        recs = recommend(affinity)

        os.makedirs("output", exist_ok=True)
        recs.to_csv("output/recommendations.csv", index=False)
        logger.info("Recommendations generated successfully!")
    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        raise

if __name__ == "__main__":
    main()
