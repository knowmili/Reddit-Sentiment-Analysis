# Reddit Sentiment Analysis CLI Tool
This Python command-line tool analyzes the sentiment of Reddit posts on a specific topic using natural language processing (NLP) techniques. It fetches posts from Reddit, preprocesses them, performs sentiment analysis, and provides insightful visualizations like sentiment score distributions and word clouds.

---

## Features
- **Fetch Posts**: Uses Reddit's API to retrieve up to 100 posts about a specified topic.
- **Preprocessing**: Cleans and preprocesses posts by removing stop words, URLs, and unwanted characters.
- **Sentiment Analysis**: Analyzes the sentiment of posts using TextBlob, generating sentiment scores.
- **CSV Export**: Saves posts and their sentiment scores in a CSV file for further analysis.
- **Visualization**: 
  - **Scatter Plot**: Displays the sentiment score distribution.
  - **Word Cloud**: Highlights the most common words in the posts.

---

## Requirements
- **Python**: `>= 3.7`
- **Python Libraries**:
  - `praw`
  - `nltk`
  - `textblob`
  - `matplotlib`
  - `wordcloud`

---

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/reddit-sentiment-analysis.git
   cd reddit-sentiment-analysis

2. Install the package dependencies
   ```pip install -r requirements.txt```

3. Install
   ```pip install .```

## Setup
1Reddit API Credentials
1. Create a Reddit app at Reddit Apps.
2. Note the following credentials:
    - Client ID
    - Client Secret
    - User Agent
3. Use these credentials when running the tool.

## Usage
```reddit-sentiment <topic> --client_id <your_client_id> --client_secret <your_client_secret> --user_agent <your_user_agent>```

## Example
```reddit-sentiment "Artificial Intelligence" --client_id myclientid --client_secret myclientsecret --user_agent myuseragent```