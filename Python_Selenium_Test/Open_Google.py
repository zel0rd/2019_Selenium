#Ch_selenium/example/tutorial1.py
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# WEBDRIVER = webdriver.Chrome('./../Chome_Driver/chromedriver')
WEBDRIVER = webdriver.Chrome('./../Chrome_Driver/chromedriver')

driver = WEBDRIVER
driver.implicitly_wait(15) # 묵시적 대기, 활성화를 최대 15초가지 기다린다.

# 페이지 가져오기(이동)
driver.get('https://google.co.kr')

# 5초후 종료
time.sleep(5)
driver.quit() # 웹 브라우저 종료. driver.close()는 탭 종료