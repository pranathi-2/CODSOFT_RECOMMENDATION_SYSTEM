import requests
import random
import pandas as pd
def fetch_latest_books(query=''):
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}&maxResults=5'
    response = requests.get(url)
    if response.status_code == 200:
        books_data = response.json()
        books = []
        for item in books_data['items']:
            title = item['volumeInfo'].get('title', 'No title')
            author = item['volumeInfo'].get('authors', ['Unknown author'])[0]
            description = item['volumeInfo'].get('description', 'No description available.')
            books.append({'title': title, 'author': author, 'description': description})
        return books
    else:
        print("Error fetching books data.")
        return []
latest_books = fetch_latest_books(query="fiction")
df_latest_books = pd.DataFrame(latest_books)
def recommend_random_book():
    if not df_latest_books.empty:
        random_book = df_latest_books.sample()
        print("Random Book Recommendation:")
        print(f"Title: {random_book['title'].values[0]}")
        print(f"Author: {random_book['author'].values[0]}")
        print(f"Description: {random_book['description'].values[0]}")
    else:
        print("No books available to recommend.")
recommend_random_book()
