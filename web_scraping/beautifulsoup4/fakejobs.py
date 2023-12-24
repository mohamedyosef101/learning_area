# The goal of this project is:
# to learn basic web scraping using beautifulsoup4

# project source: 
# https://realpython.com/beautiful-soup-web-scraper-python/

import requests as rq
from bs4 import BeautifulSoup as bs
import csv

# go to fake jobs page
url = "https://realpython.github.io/fake-jobs/"
page = rq.get(url)

# Parse HTML
soup = bs(page.content, "html.parser")

# Find elements by ID
results = soup.find(id="ResultsContainer")

# Find elements by class name
job_elements = results.find_all("div", class_="card-content")

# Create a list to store job data
jobs_data = []

# Take a look at all of the elements
for job_element in job_elements:
    title = job_element.find("h2", class_="title")
    company = job_element.find("h3", class_="company")
    location = job_element.find("p", class_="location")

    # Append the details to a list
    jobs_data.append([title.text, company.text, location.text])

# NOW run the file in the terminal by typing: 
# python fakejobs.py
    
# SAVE the outcomes
file = "jobs_data.csv"
with open(file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Writer Headers
    writer.writerow(['title', 'company', 'location'])
    # Add the other rows
    writer.writerows(jobs_data)

print(f"Data has been save to 'jobs_data.csv'")