import argparse
from reddit_sentiment_analysis.utils import preprocessPosts, findPosts, sentimentAnalysis
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import csv
import os
import nltk

def plotSentimentScores(sentiments):
    plt.scatter(range(len(sentiments)), sentiments, c=['green' if s >= 0 else 'red' for s in sentiments], alpha=0.5)
    plt.title('Sentiment Score Distribution')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    plt.axhline(0, color='grey', linestyle='--', linewidth=0.7)
    plt.grid(True)
    plt.show()

def plotWordCloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def main():
    nltk.download('stopwords')

    parser = argparse.ArgumentParser(description="Reddit Sentiment Analysis Tool")
    parser.add_argument('topic', type=str, help='Topic to fetch posts about.')
    parser.add_argument('--client_id', required=True, help='Reddit API client ID')
    parser.add_argument('--client_secret', required=True, help='Reddit API client secret')
    parser.add_argument('--user_agent', required=True, help='Reddit API user agent')
    args = parser.parse_args()

    posts = findPosts(args.topic, args.client_id, args.client_secret, args.user_agent)

    with open('posts_sentiment.csv', 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(['Post', 'Sentiment Score'])

        sentiments = []
        all_text = ""
        for post in posts:
            clean_post = preprocessPosts(post)
            sentiment = sentimentAnalysis(clean_post)
            sentiments.append(sentiment)
            all_text += " " + clean_post
            writer.writerow([clean_post, sentiment])

    print("Sentiment analysis completed. Results saved to 'posts_sentiment.csv'.")

    plotSentimentScores(sentiments)
    plotWordCloud(all_text)

if __name__ == "__main__":
    main()
