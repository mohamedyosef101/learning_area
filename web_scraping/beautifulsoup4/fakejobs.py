# The goal of this project is:
# to learn basic web scraping using beautifulsoup4

# project source: 
# https://realpython.com/beautiful-soup-web-scraper-python/

import requests as rq
from bs4 import BeautifulSoup as bs

# go to fake jobs page
url = "https://realpython.github.io/fake-jobs/"
page = rq.get(url)

# Parse HTML
soup = bs(page.content, "html.parser")

# Find elements by ID
results = soup.find(id="ResultsContainer")

# Use prettify for easier viewing.
print(results.prettify())

# NOW run the file in the terminal by typing: 
# python fakejobs.py
