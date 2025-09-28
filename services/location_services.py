import pandas as pd

def get_location():
    df = pd.read_csv(r"C:\Users\Yash\Desktop\CS\Projects\FraudDetection\Data\combined_data.csv")
    locations = list(df[df["is_fraud"] == 1][["merch_lat", "merch_long"]].itertuples(index=False, name=None))
    return locations