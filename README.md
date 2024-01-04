Simple Amazon web scraper using BeautifulSoup in Python.

This Python script uses BeautifulSoup and requests to create a simple web scraper for Amazon's best-selling electronics.

The script sends an HTTP request to the provided Amazon URL, extracts relevant product details such as title and price, and stores them in a list of dictionaries.

Finally, the script saves the gathered data to a JSON file named 'amazon_top_selling.json'. Adjustments may be necessary if Amazon's HTML structure changes.

usage:

First, make sure to install the required libraries.

pip install requests beautifulsoup4
