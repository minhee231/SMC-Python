from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def main(ser):
    driver = webdriver.Chrome()
    url = f"https://www.youtube.com/results?search_query={ser}"
    driver.get(url)
    time.sleep(0.3)

    
    eles = driver.find_elements(By.CSS_SELECTOR,'#video-title > yt-formatted-string')
    eles = driver.find_elements(By.CSS_SELECTOR,'#video-title')
    for i in range(10):
        print(eles[i].text)
        print(eles[i].get_attribute("href"))

    # for ele in eles:
    #     print(ele.text)

    

main("MyGO!!!!!")
