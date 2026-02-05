# test_pipeline.py
import sys
import os
sys.path.append('src')

from main import main

if __name__ == "__main__":
    try:
        main()
        print("Pipeline completed successfully!")
    except Exception as e:
        print(f"Pipeline failed: {e}")
        sys.exit(1)