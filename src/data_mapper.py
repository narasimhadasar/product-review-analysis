# src/data_mapper.py
def map_columns(df):
    """Map CSV columns to expected format"""
    column_mapping = {
        'reviews.text': 'review_text',
        'categories': 'category'
    }
    
    df = df.rename(columns=column_mapping)
    
    # Extract main category from categories string
    if 'category' in df.columns:
        df['category'] = df['category'].str.split(',').str[0]
    
    return df