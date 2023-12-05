from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

driver = webdriver.Chrome()

Search_KeyWord = input("keyword :").replace(' ', '+')

url = f"https://www.youtube.com/results?search_query={Search_KeyWord}"
driver.get(url)

selector = "#video-title"
titles = driver.find_elements(By.XPATH,'//*[@id="video-title"]')

datalist = []
for title in titles:
    data = {}
    item_name = title.text
    url = title.get_attribute('href')
    print(url)
    
    if url:
        data["title"] = title.get_attribute('title')
        data["url"] = title.get_attribute('href')
        datalist.append(data)
    else:
        continue

    df = pd.DataFrame(datalist)

    df.to_excel("youtube.xlsx")