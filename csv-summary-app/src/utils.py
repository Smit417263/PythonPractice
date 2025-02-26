def read_csv(file_path):
    import pandas as pd
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return None

def summarize_data(data):
    if data is None or data.empty:
        return "No data to summarize."
    
    summary = {}
    summary['columns'] = list(data.columns)
    summary['num_rows'] = len(data)
    summary['data_types'] = data.dtypes.to_dict()
    summary['description'] = data.describe(include='all').to_dict()
    
    return summary