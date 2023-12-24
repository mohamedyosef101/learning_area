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

# Find elements by class name
job_elements = results.find_all("div", class_="card-content")

# Take a look at all of the elements
for job_element in job_elements:
    title = job_element.find("h2", class_="title")
    company = job_element.find("h3", class_="company")
    location = job_element.find("p", class_="location")

    # view all of it
    print(f"""------------------
        \nTitle: {title.text}
        \nCompany: {company.text}
        \nLocation: {location.text}
""")

# NOW run the file in the terminal by typing: 
# python fakejobs.py
