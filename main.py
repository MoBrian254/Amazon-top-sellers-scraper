import requests
from bs4 import BeautifulSoup
import json

def scrape_amazon(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        products = []

        for product in soup.find_all('div', {'class': 's-result-item'}):
            # Extract relevant details (modify as needed)
            title = product.find('span', {'class': 'a-text-normal'}).text.strip()
            price = product.find('span', {'class': 'a-offscreen'})
            price = price.text.strip() if price else 'N/A'

            # Store details in a dictionary
            product_info = {
                'title': title,
                'price': price
            }

            products.append(product_info)

        # Save to a JSON file
        with open('amazon_top_selling.json', 'w') as json_file:
            json.dump(products, json_file, indent=2)

        print('Scraping successful. Data saved to amazon_top_selling.json')
    else:
        print(f'Error: {response.status_code}')

# Example usage
amazon_url = 'https://www.amazon.com/best-sellers-electronics/zgbs/electronics/'
scrape_amazon(amazon_url)
