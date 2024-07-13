import requests
from bs4 import BeautifulSoup
import json

# Функція для отримання даних про цитати
def scrape_quotes():
    quotes = []
    authors = []
    url = "http://quotes.toscrape.com"
    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for quote in soup.select(".quote"):
            text = quote.select_one(".text").get_text()
            author = quote.select_one(".author").get_text()
            tags = [tag.get_text() for tag in quote.select(".tags .tag")]

            quotes.append({
                "quote": text,
                "author": author,
                "tags": tags
            })

            author_url = quote.select_one(".author + a")["href"]
            author_response = requests.get(f"http://quotes.toscrape.com{author_url}")
            author_soup = BeautifulSoup(author_response.text, "html.parser")

            fullname = author_soup.select_one(".author-title").get_text()
            born_date = author_soup.select_one(".author-born-date").get_text()
            born_location = author_soup.select_one(".author-born-location").get_text()
            description = author_soup.select_one(".author-description").get_text()

            authors.append({
                "fullname": fullname,
                "born_date": born_date,
                "born_location": born_location,
                "description": description
            })

        next_page = soup.select_one(".next > a")
        url = f"http://quotes.toscrape.com{next_page['href']}" if next_page else None

    return quotes, authors

# Збереження даних в JSON файли
quotes, authors = scrape_quotes()
with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(quotes, f, ensure_ascii=False, indent=4)

with open("authors.json", "w", encoding="utf-8") as f:
    json.dump(authors, f, ensure_ascii=False, indent=4)
