import requests
from bs4 import BeautifulSoup
import csv

# URL of the website to scrape (books.toscrape.com)
BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

# CSV file to store results
filename = "books_data.csv"
header = ["Title", "Price", "Rating"]

# Open CSV file
with open(filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(header)

    # Loop through first 5 pages (you can increase)
    for page in range(1, 6):
        print(f"Scraping Page {page}...")
        response = requests.get(BASE_URL.format(page))
        soup = BeautifulSoup(response.content, "html.parser")
        books = soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text.replace("£", "")
            rating = book.p["class"][1]  # Rating class name e.g., 'Three'

            writer.writerow([title, price, rating])

print("✅ Data scraped and saved to 'books_data.csv'")
