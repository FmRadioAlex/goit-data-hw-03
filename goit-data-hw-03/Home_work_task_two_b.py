from pymongo import MongoClient
import json

# Підключення до MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['quotes_database']

# Імпорт даних в колекції MongoDB
with open("quotes.json", "r", encoding="utf-8") as f:
    quotes = json.load(f)
    db.quotes.insert_many(quotes)

with open("authors.json", "r", encoding="utf-8") as f:
    authors = json.load(f)
    db.authors.insert_many(authors)
