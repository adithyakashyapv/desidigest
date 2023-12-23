import pandas as pd
import requests
import apiKeys


api_key = apiKeys.newsIoApiKey

def extract_news():
    newsapi_url = f'https://newsdata.io/api/1/news?apikey={api_key}&language=en&country=in'

    response = requests.get(newsapi_url)

    if response.status_code == 200:
        data = response.json()

        articles = [{'Title': article['title'], 'Content': article['content'], 'SourceID': article['source_id']} for article in data['results']]
        df = pd.DataFrame(articles)

        df.to_csv('news_articles_full.csv', index=False)

def main():
    extract_news()


if __name__ == "__main__":
    main()