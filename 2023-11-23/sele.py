from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://mail.naver.com")

time.sleep(2)

title = driver.title
print(title)

url = driver.current_url
print(url)

login_url = ' nid.naver.com'

element = driver.find_element(By.XPATH, '//input[@placeholder="아이디"]')
element.send_keys("Your ID")
time.sleep(0.2)
element = driver.find_element(By.XPATH, '//input[@placeholder="비밀번호"]')
element.send_keys("Your PassWord")
element.send_keys(Keys.RETURN)


time.sleep(1000000)

