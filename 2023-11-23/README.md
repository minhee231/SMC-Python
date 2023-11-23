## 대기(Driver wait)
* time.sleep(3) 은 대기하는 것으로 적절치 않음
* 네트워크 및 시스템 상태에 따라 2초가 적합할지 10초가 적합할지 알 수 없음
* WebDriverWait, expected_conditions 필요
* from selenium.webdriver.support.ui import WebDriverWait 필요
* from selenium.webdriver.support.ui import expected_conditions as EC
* 이런 기능으로 인해 Selenium은 동적인 사이트를 다루는데 유용함.
* 개발자 도구에서 Network 속도를 느리게 하여 테스트 가능함