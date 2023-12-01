from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
import time

driver = webdriver.Chrome()
sea = 'fender american original 60s telecaster lake placid blue'.replace(' ','+')
url = f'https://www.google.com/search?q={sea}&tbm=isch'

driver.get(url)
time.sleep(1)

# for i in range(5):
#     element = driver.find_element(By.XPATH, f'//*[@data-ri="{i}"]')
#     element.click()
#     time.sleep(2)

elements = driver.find_elements(By.XPATH, f'//*[@data-ri]')
flag = 0
for element in elements:
    ele = element.find_element(By.TAG_NAME,'img')
    print(ele.get_attribute('alt'))
    imgurl = ele.get_attribute('src')
    urllib.request.urlretrieve(imgurl,f"{sea}{flag}.jpg")
    element.click()
    time.sleep(0.2)
    flag+=1

    # if flag > 20:
    #     break
