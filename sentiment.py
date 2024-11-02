import requests
from bs4 import BeautifulSoup
from transformers import pipeline
import matplotlib.pyplot as plt
import numpy as np

def scrape_article_data(url):
    """Scrape headlines and articles from a given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        headlines = [h.get_text() for h in soup.find_all('h2')]  # Modify based on the website's structure
        articles = [p.get_text() for p in soup.find_all('p')]    # Modify as needed

        return headlines, articles
    except Exception as e:
        print(f"Error scraping data: {e}")
        return [], []

def preprocess_text(text):
    """Preprocess the text for analysis."""
    return text.replace('\n', ' ').strip()

def analyze_sentiment(text, keyword, sentiment_pipeline):
    """Analyze sentiment of the text based on the keyword using a sentiment analysis model."""
    if keyword.lower() in text.lower():
        result = sentiment_pipeline(text)
        return result[0]['score'] * (1 if result[0]['label'] == 'POSITIVE' else -1)
    return None  # No sentiment score if keyword is not present

def visualize_sentiment(sentiments, keyword):
    """Visualize the sentiment scores."""
    if not sentiments:
        print(f"No sentiment data to visualize for '{keyword}'.")
        return

    plt.figure(figsize=(10, 5))
    plt.hist(sentiments, bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Sentiment Distribution for "{keyword}"')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    plt.axvline(0, color='red', linestyle='dashed', linewidth=1)
    plt.show()

def main(urls, keyword):
    """Main function to scrape, analyze, and visualize sentiment for multiple URLs."""
    sentiment_pipeline = pipeline("sentiment-analysis")

    all_sentiments = []

    for url in urls:
        print(f"Scraping: {url}")
        headlines, articles = scrape_article_data(url)

        all_text = [preprocess_text(text) for text in headlines + articles]

        for text in all_text:
            sentiment = analyze_sentiment(text, keyword, sentiment_pipeline)
            if sentiment is not None:
                all_sentiments.append(sentiment)

    if all_sentiments:
        average_sentiment = np.mean(all_sentiments)
        print(f"Average sentiment for '{keyword}': {average_sentiment:.2f}")
        visualize_sentiment(all_sentiments, keyword)
    else:
        print(f"No mentions of '{keyword}' found in the articles.")

# Example usage
if __name__ == "__main__":
    urls = [
        'https://example.com/news',  # Replace with actual URLs
        'https://anotherexample.com/news'  # Add more sources as needed
    ]
    keyword = 'AAPL'  # Replace with the stock ticker or company name you're interested in
    main(urls, keyword)
