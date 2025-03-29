## Project Intro

This project aims to analyze the relationship between the polarity of Elon Musk's tweets and the performance of Tesla's stock prices. By leveraging sentiment analysis on the tweets, we can gain insights into how Elon Musk’s online presence influences stock market behavior.

## What to Expect

- **Data Collection**: The project uses a dataset of Elon Musk's tweets from 2010 to 2025.
- **Sentiment Analysis**: Tweets are processed using Natural Language Processing (NLP) techniques, specifically **VADER** (Valence Aware Dictionary and sEntiment Reasoner), to score the sentiment (polarity) of each tweet.
- **Stock Price Analysis**: The sentiment scores are then compared to Tesla’s stock price on the following day, to explore possible correlations.

## Dataset

This project requires a dataset that is referenced in the `config.yaml` file. Since the dataset is not included in the GitHub repository, follow the steps below to obtain it.

1. **Download the Dataset:**
   - You can download the dataset from the following link:  
     [Download Dataset from Kaggle](https://www.kaggle.com/datasets/dadalyndell/elon-musk-tweets-2010-to-2025-march)

2. **Set the Dataset Path:**
   - After downloading the dataset, ensure that the `config.yaml` file points to the correct path where you saved the CSV file.
   
   Example:
   ```yaml
   data_path: "/path/to/your/dataset.csv"
