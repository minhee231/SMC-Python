from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

driver = webdriver.Chrome()

url = f"https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query={input('keyword : ').replace('','+')}"
driver.get(url)

newsss = driver.find_elements(By.XPATH,'//*[@class="news_tit"]')

datas = []
for news in newsss:
    data = {}
    data["title"] = news.get_attribute('title')
    data["url"] = news.get_attribute('href')
    datas.append(data) 

    df = pd.DataFrame(datas)

    df.to_excel("naver.xlsx")