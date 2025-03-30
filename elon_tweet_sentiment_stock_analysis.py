import pandas as pd
import yaml
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Load the configuration file
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Use the path from the config file
file_path = config["data_path"]

# Read the CSV using the file path from the config
df = pd.read_csv(file_path, low_memory=False)

# # Download VADER lexicon (if first time using it)
# nltk.download("vader_lexicon")

# Initialize the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Function to calculate sentiment score for a tweet
def get_sentiment_score(tweet):
    sentiment = sia.polarity_scores(tweet)
    return sentiment["compound"]  # Compound score is a summary metric

# Apply sentiment analysis to the tweet column and create a new column
df["sentiment_score"] = df["fullText"].apply(get_sentiment_score)

# Sort the DataFrame by 'sentiment_score' in descending order and print the top 5
top_5_sentiments = df.sort_values(by='sentiment_score', ascending=False).head(5)

# Print the top 5 rows
print(top_5_sentiments)
