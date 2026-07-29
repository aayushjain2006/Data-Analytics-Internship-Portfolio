import pandas as pd

def load_data():
    """
    Load the cleaned Superstore dataset
    """
    file_path = "data/superstore_cleaned.xlsx"
    df = pd.read_excel(file_path)
    return df