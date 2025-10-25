import requests

def get_news():
    try:
        url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=demo"
        response = requests.get(url)
        data = response.json()
        headlines = [article['title'] for article in data['articles'][:5]]
        return headlines
    except:
        return ["Unable to fetch news right now."]
