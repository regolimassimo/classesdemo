import requests
from bs4 import BeautifulSoup

conn = requests.get("https://www.ansa.it/sito/notizie/economia/economia.shtml")
html = conn.text

soup = BeautifulSoup(html, "html.parser")
scripts = soup.find_all("script")
articles = soup.find_all("article", {"class": "news"})
for article in articles:
    js = article.find("script")
    print(article.encode_contents())