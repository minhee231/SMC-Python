from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


driver = webdriver.Chrome()
query = "fender telecaster"
query = query.replace(" ","+")
page = 1
item_name = ""

url = f"https://search.shopping.naver.com/search/all?pagingIndex={page}&pagingSize=40&productSet=total&query={query}&sort=rel&timestamp=&viewType=list"
driver.get(url)

time.sleep(1)
driver.execute_script("window.scrollTo(0, 10000);")

elements = driver.find_element(By.CSS_SELECTOR,"#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div > div:nth-child(1) > div > div > div.adProduct_info_area__dTSZf > div.adProduct_title__amInq > a")
item_code = elements.get_attribute("data-i")
data = elements.get_attribute("data-nclick")
rang = data.split(f"{item_code},r:")[1]

print(f"{query} 키워드로 검색시 {page}페이지에서 검색되었으며 {rang}위 입니당")
time.sleep(10000)