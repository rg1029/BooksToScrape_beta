import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape book information from a page
def scrape_books(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    scraped_data = []

    for book in books:
        title = book.h3.a.attrs['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        scraped_data.append([title, price, availability])

    return scraped_data

# Function to export data to a CSV file
def export_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title', 'Price', 'Availability'])
        writer.writerows(data)

# Main function to execute the scraping and exporting
def main():
    base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
    num_pages = 5  # Number of pages you want to scrape
    all_books = []

    for page in range(1, num_pages + 1):
        url = base_url.format(page)
        all_books.extend(scrape_books(url))

    export_to_csv(all_books, 'books_data.csv')
    print("Scraping completed and data exported to 'books_data.csv'.")

if __name__ == "__main__":
    main()
#new comment 