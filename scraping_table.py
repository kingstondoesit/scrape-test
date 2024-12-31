# Scraping Wikipedia Table

from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

soup.find('table', class_='wikitable sortable')

table1 = soup.find_all('table')[0]

# print(table1.prettify())

world_titles = table1.find_all('th')

world_table_titles = [title.text.strip() for title in world_titles]

import pandas as pd

df = pd.DataFrame(columns=world_table_titles)

column_data = table1.find_all("tr")

for row in column_data[1:]:  # Skip the first row  
    row_data = row.find_all('td')  
    individual_data = [data.text.strip() for data in row_data]  
    
    if len(individual_data) == len(df.columns):  # Ensure we have the right number of columns  
        df.loc[len(df)] = individual_data  # Append to the DataFrame  
        
    print(individual_data)  

df.to_csv(r'scraped_table_wikipedia1.csv', index=False)
