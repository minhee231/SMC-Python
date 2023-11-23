from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

url = "https://www.naver.com"
driver = webdriver.Chrome()
driver.get(url)

css_selector = "#newsstand > div.ContentHeaderSubView-module__content_header_sub___Yszwk"

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

#증시 텍스트 출력
element = driver.find_element(By.CLASS_NAME,"DailyBoardView-module__stock_name___s9Qlh")
print(element.text)            