from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
search = input("검색어").replace(' ','+')

driver.get(f'https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query={search}')
time.sleep(1)

elements = driver.find_elements(By.CSS_SELECTOR,"a.news_tit")

for element in elements:
    print(f'{element.text} : {element.get_attribute("href")}')