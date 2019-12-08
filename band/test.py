## zel0rd 

import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pytube import YouTube
from selenium import webdriver as wd

# get current path
# currentPath = os.getcwd()

# change path
# os.chdir('/Users/guest/Desktop')


print("Start program")

current_path = os.getcwd()
print(current_path)
driver_path = current_path + '\chromedriver.exe'
print(driver_path)
driver = wd.Chrome(executable_path=driver_path)
driver.implicitly_wait(5)

url = "https://www.naver.com"
driver.get(url)
time.sleep(1)

url = "https://band.us/discover/search/%EC%A3%BC%EC%8B%9D"
driver.get(url)
driver.find_element_by_id("input_search_view87").clear()
driver.find_element_by_id("input_search_view87").send_keys('증권')
driver.find_element_by_css_selector("button.btnSearch").click()

elem = driver.find_element_by_tag_name("body")
pagedowns = 1
while pagedowns < 10:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
        pagedowns += 1

time.sleep(5)

driver.find_element_by_id("input_search_view87").clear()
driver.find_element_by_id("input_search_view87").send_keys('주식')
driver.find_element_by_css_selector("button.btnSearch").click()

time.sleep(5)



def get_links():
#    req = requests.get(url)
#    html = req.text
    html = driver.page_source
    soup = BeautifulSoup(html)
#    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select(
        '.cCoverItem>href'
        )

    links = []
    for title in my_titles:
    #    print(title.text)
    #    print(title.get('href'))
        links.append("https://www.band.us/"+title.get('href'))

    print(links)
    print(len(links))
    return links


links = get_links()
print(links)

# url = ''
# DRIVER_DIR=""


# def get_links():
# #    req = requests.get(url)
# #    html = req.text
#     html = driver.page_source
#     soup = BeautifulSoup(html)
# #    soup = BeautifulSoup(html, 'html.parser')
#     my_titles = soup.select(
#         'h3 > a'
#         )

#     links = []
#     for title in my_titles:
#     #    print(title.text)
#     #    print(title.get('href'))
#         links.append("https://www.youtube.com/"+title.get('href'))

#     print(links)
#     print(len(links))
#     return links

# driver = webdriver.Chrome(DRIVER_DIR)
# driver.implicitly_wait(5)
# driver.get(url)
# elem = driver.find_element_by_tag_name("body")

# pagedowns = 1
# while pagedowns < 100:
#         elem.send_keys(Keys.PAGE_DOWN)
#         time.sleep(0.1)
#         pagedowns += 1

# links = get_links()

# for link in links:
#     YouTube(link).streams.first().download()
#     print("Download complete " + str(links.index(link) + 1) + "/" + str(len(links)) )