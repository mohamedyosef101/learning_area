import csv
import re

# Read the problematic CSV file
input_file = 'web_scraping/beautifulsoup4/jobs_data.csv'  
output_file = 'web_scraping/beautifulsoup4/cleaned_jobs_data.csv'

with open(input_file, 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    rows = list(reader)

# Clean up the data
cleaned_rows = []
for row in rows:
    cleaned_row = [item.strip() if isinstance(item, str) else item for item in row]
    cleaned_row = [re.sub(r'\s+', ' ', col) for col in cleaned_row]  # Remove extra spaces and newlines
    cleaned_rows.append(cleaned_row)

# Write cleaned data to a new CSV file
with open(output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Company', 'Location'])  # Write header
    writer.writerows(cleaned_rows)

print(f"Data has been cleaned and saved to '{output_file}'")
