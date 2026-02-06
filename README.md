**Product Review Analysis - Sentiment-Driven Recommendations**

ML pipeline for analyzing customer reviews and generating sentiment-based product recommendations.

*Features

- **Sentiment Analysis**: VADER sentiment analysis on customer reviews
- **Brand/Category Extraction**: Automated extraction from structured data
- **Recommendation Engine**: Sentiment-driven product recommendations
- **Dockerized Deployment**: Container-ready for easy deployment

### Option 1: Docker (Recommended)
```bash
# Clone repository
git clone <your-repo-url>
cd product-review-analysis

# Build and run with Docker
docker build -t product-review-analysis .
docker run product-review-analysis
```

### Option 2: Python Direct
```bash
# Install dependencies
pip install -r requirements.txt

# Run pipeline
python test_pipeline.py
```

## Results

Output: `output/recommendations.csv` with brand-category recommendations ranked by sentiment scores.

**Sample Results:**
- The Laundress (Household) - 93% positive sentiment
- Happy Family (Food) - 93% positive sentiment
- Weleda (Personal Care) - 89% positive sentiment

## Architecture

```
src/
├── main.py              # Main pipeline orchestrator
├── data_loader.py       # CSV data loading
├── data_mapper.py       # Column mapping
├── preprocessing.py     # Text preprocessing
├── sentiment.py         # VADER sentiment analysis
├── affinity.py         # Brand-category affinity calculation
└── recommender.py      # Recommendation generation
```

## Requirements

- Python 3.10+
- pandas, numpy, vaderSentiment
- Docker 

##  Validation

The pipeline processes 50K+ reviews and generates actionable recommendations. Success metrics:
-  Sentiment scores: -1 to +1 range
-  Review count filtering: Minimum threshold applied
-  Brand-category coverage: 100+ combinations analyzed

##  ML Pipeline

1. **Data Ingestion**: Load review data
2. **Preprocessing**: Clean and map columns  
3. **Sentiment Analysis**: Extract sentiment scores
4. **Affinity Calculation**: Compute brand-category preferences
5. **Recommendation Generation**: Rank by sentiment
6. **Output**: CSV with actionable insights
