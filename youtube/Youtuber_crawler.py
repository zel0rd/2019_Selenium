# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 22:56:35 2019

@author: ZELORD
"""

import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pytube import YouTube

url = 'https://www.youtube.com/user/TOSSservice/videos'
DRIVER_DIR= './chromedriver.exe'

def get_links():
#    req = requests.get(url)
#    html = req.text
    html = driver.page_source
    soup = BeautifulSoup(html)
#    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select(
        'h3 > a'
        )

    links = []
    for title in my_titles:
    #    print(title.text)
    #    print(title.get('href'))
        links.append("https://www.youtube.com/"+title.get('href'))

    print(links)
    print(len(links))
    return links

driver = webdriver.Chrome(DRIVER_DIR)
driver.implicitly_wait(5)
driver.get(url)
elem = driver.find_element_by_tag_name("body")

pagedowns = 1
while pagedowns < 100:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
        pagedowns += 1

links = get_links()

for link in links:
    YouTube(link).streams.first().download()
    print("Download complete " + str(links.index(link) + 1) + "/" + str(len(links)) )
