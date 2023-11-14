from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = 'https://naver.com'
driver = webdriver.Chrome()

driver.get(url)


driver.find_element(By.CLASS_NAME,"search_input").send_keys("파이썬" + Keys.ENTER)


driver.find_element(By.NAME,"query").clear
driver.find_element(By.NAME,"query").send_keys("세명컴고" + Keys.ENTER)

png = driver.get_screenshot_as_png()
open('search_result.png', 'wb').write(png)