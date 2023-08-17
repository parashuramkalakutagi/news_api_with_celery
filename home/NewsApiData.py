import requests
from .models import NewsBusiness,journal


def News_data():
    api_key = "8fcd2cf2bb714009946c82498a38e906"
    url = f"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={api_key}"

    result = requests.get(url)
    rs = result.json()

    for article in rs['articles']:
        NewsBusiness.objects.create(
            author = article['author'],
            title=article['title'],
            description = article['description'],
            url=article['url'],
            urlToImage=article['urlToImage'],
            publishedAt=article['publishedAt'],
            content=article['content'],
        )

    return rs


def jaurnal():
    api_key = "8fcd2cf2bb714009946c82498a38e906"
    url = f"https://newsapi.org/v2/everything?domains=wsj.com&apiKey={api_key}"

    result = requests.get(url)
    rs = result.json()

    for article in rs['articles']:

        journal.objects.create(
            author = article['author'],
            title=article['title'],
            description = article['description'],
            url=article['url'],
            urlToImage=article['urlToImage'],
            publishedAt=article['publishedAt'],
            content=article['content'],
        )

    return rs


