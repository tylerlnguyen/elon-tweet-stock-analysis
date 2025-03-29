import pandas as pd
import yaml

# Load the configuration file
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Use the path from the config file
file_path = config["data_path"]

# Read the CSV using the file path from the config
df = pd.read_csv(file_path)

# Print the first few rows of the dataframe
print(df.head())
