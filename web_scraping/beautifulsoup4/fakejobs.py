# The goal of this project is:
# to learn basic web scraping using beautifulsoup4

# project source: 
# https://realpython.com/beautiful-soup-web-scraper-python/

import requests as rq

# go to fake jobs page
url = "https://realpython.github.io/fake-jobs/"
page = rq.get(url)
print(page.text)

# NOW run the file in the terminal by typing: 
# python fakejobs.py
