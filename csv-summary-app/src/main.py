import pandas as pd
import kagglehub
from pathlib import Path

def main():
    try:
        path = kagglehub.dataset_download("ankushpanday2/heart-attack-risk-and-prediction-dataset-in-india")
        print("Path to dataset files:", path)
        
        data = read_csv(Path(path))
        summary = summarize_data(data)
        print(summary)
    except Exception as e:
        print(f"An error occurred: {e}")

def read_csv(path):
    # Assuming the dataset contains a single CSV file
    csv_file = [f for f in path.iterdir() if f.suffix == '.csv'][0]
    return pd.read_csv(csv_file)

def summarize_data(data):
    summary = {
        "columns": data.columns.tolist(),
        "shape": data.shape,
        "head": data.head().to_dict(orient='records'),
        "description": data.describe(include='all').to_dict()
    }
    return summary

if __name__ == "__main__":
    main()