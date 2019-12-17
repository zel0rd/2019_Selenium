# selenium tutorial

# 1. vscode settings
## vscode cmd + shift + p
## install extensions
## python / python for vscode / python extension pack / pydev (4)

# 2. selenium library settings
## selenium docs : https://selenium-python.readthedocs.io/installation.html#downloading-python-bindings-for-selenium
## pip install selenium

# 3. download browser driver
### download chrome driver (!check chrome version)
### download phantomjs driver https://brownbears.tistory.com/424, https://phantomjs.org/download.html (optional)

# 4. architecture design
## band.us 페이지로 이동
## 특정 밴드로 이동
## 검색에 "주식" or "증권" 검색
## 검색내용 중 "갈림길 페이지" or "갈림길 밴드"를 클릭
## 반복

# 5. CODE

import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver as wd

# band 검색

# 시작부분
url = "https://www.naver.com"

# 주식_밴드
url_stock_band = "https://band.us/discover/band-search/%EC%A3%BC%EC%8B%9D"
# 주식_페이지
url_stock_page = "https://band.us/discover/page-search/%EC%A3%BC%EC%8B%9D"
# 증권_밴드
url_fund_band = "https://band.us/discover/band-search/%EC%A6%9D%EA%B6%8C"
# 증권_페이지
url_fund_page = "https://band.us/discover/page-search/%EC%A6%9D%EA%B6%8C"

current_path = os.getcwd()
driver_path = current_path + '\..\driver\chromedriver.exe'

# 주식 - 밴드
def stock_band():
    driver = wd.Chrome(executable_path=driver_path)

    driver.get(url)
    driver.implicitly_wait(5)
    time.sleep(1)

    print("stock_band")
    driver.get(url_stock_band)
    driver.implicitly_wait(5)

    # page_down_function
    elem = driver.find_element_by_tag_name("body")
    pagedowns = 1
    while pagedowns < 5:
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.1)
            pagedowns += 1

    leader_list = driver.find_elements_by_css_selector('.cCoverList>.cCoverItem')

    for i in range(len(leader_list)):
        name = leader_list[i].find_element_by_css_selector('.bandUri>.bandName>.member>.leader').text
        print(name)
        if name == "리더 갈림길":
            print("'주식 밴드' 검색 순위 : ",(i+1))
            leader_list[i].find_element_by_css_selector('a').send_keys(Keys.ENTER)
            time.sleep(3)
            break
    driver.quit()

            


# 증권 - 밴드
def fund_band():
    print("fund_band")    
    driver = wd.Chrome(executable_path=driver_path)

    driver.get(url)
    driver.implicitly_wait(5)
    time.sleep(1)

    driver.get(url_fund_band)
    driver.implicitly_wait(5)

    # page_down_function
    elem = driver.find_element_by_tag_name("body")
    pagedowns = 1
    while pagedowns < 5:
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.1)
            pagedowns += 1

    leader_list = driver.find_elements_by_css_selector('.cCoverList>.cCoverItem')

    for i in range(len(leader_list)):
        name = leader_list[i].find_element_by_css_selector('.bandUri>.bandName>.member>.leader').text
        print(name)
        if name == "리더 갈림길":
            print("'증권 밴드' 검색 순위 : ",(i+1))
            leader_list[i].find_element_by_css_selector('a').send_keys(Keys.ENTER)
            time.sleep(3)
            break
    driver.quit()

# 주식 - 페이지
def stock_page():
    print("stock_page")
    driver = wd.Chrome(executable_path=driver_path)

    driver.get(url)
    driver.implicitly_wait(5)
    time.sleep(1)

    driver.get(url_stock_page)
    driver.implicitly_wait(5)

    # page_down_function
    elem = driver.find_element_by_tag_name("body")
    pagedowns = 1
    while pagedowns < 5:
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.1)
            pagedowns += 1
    
    leader_list = driver.find_elements_by_css_selector('.cCoverList>.cCoverItem')

    for i in range(len(leader_list)):
        name = leader_list[i].find_element_by_css_selector('a').text
        print(name)
        if name == "주식은 갈림길":
            print("'주식 페이지' 검색 순위 : ",(i+1))
            leader_list[i].find_element_by_css_selector('a').send_keys(Keys.ENTER)
            time.sleep(3)
            break
    driver.quit()
    

# 증권 - 페이지
def fund_page():
    print("fund_page")

    driver = wd.Chrome(executable_path=driver_path)

    driver.get(url)
    driver.implicitly_wait(5)
    time.sleep(1)

    driver.get(url_fund_page)
    driver.implicitly_wait(5)

    # page_down_function
    elem = driver.find_element_by_tag_name("body")
    pagedowns = 1
    while pagedowns < 5:
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.1)
            pagedowns += 1

    leader_list = driver.find_elements_by_css_selector('.cCoverList>.cCoverItem')
    
    for i in range(len(leader_list)):
        name = leader_list[i].find_element_by_css_selector('a').text
        print(name)
        if name == "주식은 갈림길":
            print("'증권 페이지' 검색 순위 : ",(i+1))
            leader_list[i].find_element_by_css_selector('a').send_keys(Keys.ENTER)
            time.sleep(3)
            break
    driver.quit()
    
while True:
    stock_band()
    fund_band()
    stock_page()
    fund_page()