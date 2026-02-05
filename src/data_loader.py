# src/data_loader.py
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def load_data(path):
    try:
        df = pd.read_csv(path)
        logger.info(f"Dataset loaded: {df.shape}")
        logger.info(f"Columns: {list(df.columns)}")
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"Data file not found: {path}")
    except Exception as e:
        raise Exception(f"Error loading data: {e}")
