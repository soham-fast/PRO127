from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars"

# Webdriver
browser = webdriver.Edge()
browser.get(START_URL)

time.sleep(10)

#Define Scrape function
scrape_data = []

# Define Exoplanet Data Scrapping Method
def scrape():
    soup=BeautifulSoup(browser.page_source,"html.parser")
    bright_star_table=soup.find("table",attrs=("class","wikitable sortable jquery-tablesorter"))
    table_body=bright_star_table.find("tbody")
    table_rows=table_body.find_all("tr")
    for row in table_rows:
        table_cols=row.find_all("td")
        #print(table_cols)
        templis=[]
        for cols in table_cols:
            data=cols.text.strip()
            print(data)
            templis.append(data)
        scrape_data.append(templis)
          
scrape()     
    
headers=["c1","c2","c3","c4","c5","c6"]

stars_data=pd.DataFrame(scrape_data,columns=headers)
stars_data.to_csv("scraped_data.csv",index=True ,index_label="id")





