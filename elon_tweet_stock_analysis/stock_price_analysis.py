import pandas as pd
import yaml

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

stocks_data_path = config["stocks_data_path"]

stocks_df = pd.read_csv(stocks_data_path, low_memory=False)

print("\nTesla Stock Data:")
print(stocks_df.head())