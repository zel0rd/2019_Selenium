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
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pytube import YouTube

DRIVER_DIR = './chromedriver.exe'
CGV_LOGIN_URL = "https://www.cgv.co.kr/user/login/"
CGV_ID = ""
CGV_PW = ""
DATE = "20211227"
CGV_RESERVATION_URL = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=" + \
    DATE + "&screencodes=&screenratingcode=02"
MOVIE_NAME = "스파이더맨"
# SCREEN_TIME
IS_SCREEN = False
MY_MOVIE_ELEMENT = ""
RESERVATION_TIME = "12:00"


def openBrowser():
    global driver
    driver = webdriver.Chrome(DRIVER_DIR)
    driver.implicitly_wait(5)


def loginCGV():
    global driver
    driver.get(CGV_LOGIN_URL)
    driver.implicitly_wait(5)
    driver.find_element_by_css_selector('#txtUserId').send_keys(CGV_ID)
    driver.find_element_by_css_selector('#txtPassword').send_keys(CGV_PW)
    driver.find_element_by_css_selector('#txtPassword').send_keys(Keys.ENTER)


def findMOIVE():
    global driver
    global IS_SCREEN
    global MY_MOVIE_ELEMENT
    # IS_SCREEN CHECKING
    while not IS_SCREEN:
        print("### 상영여부 확인중 ###")
        driver.get(CGV_RESERVATION_URL)
        driver.implicitly_wait(5)
        moviesElements = driver.find_elements_by_css_selector(
            ".info-movie > a > strong")

        print("### 상영중인 영화  ###")

        for movieElement in moviesElements:
            print(movieElement.text)
            if MOVIE_NAME in movieElement.text:
                MY_MOVIE_ELEMENT = movieElement
                IS_SCREEN = True

        print("####################")

        time.sleep(1)


def isEarlier(time1, time2):
    print(time1, time2)
    time1_sec = int(time1.split(":")[0]) * 60 + int(time1.split(":")[1])
    time2_sec = int(time2.split(":")[0]) * 60 + int(time2.split(":")[1])

    return True if time1_sec < time2_sec else False


def checkTime():
    global MY_MOVIE_ELEMENT
    global RESERVATION_TIME
    screen_times = MY_MOVIE_ELEMENT.find_element_by_xpath('..').find_element_by_xpath(
        '..').find_element_by_xpath('..').find_elements_by_css_selector('.info-timetable > ul > li')

    link = ''
    for screen_time in screen_times:
        print("AA", screen_time.text.split("\n")[0], "BB", RESERVATION_TIME)
        if not isEarlier(screen_time.text.split("\n")[0], RESERVATION_TIME) and link == '':
            link = screen_time

    link.click()


def selectSeat():
    driver.implicitly_wait(5)
    driver.switch_to.frame("ticket_iframe")
    time.sleep(3)
#     print(driver.find_element_by_css_selector("#tnb_step_btn_right").text)
    driver.find_element_by_css_selector("#tnb_step_btn_right").click()
#     print("CLICKED")


def closePopup():
    title_area = driver.find_element_by_css_selector("title_area")
    title_area.find_elements_by_css_selector("a").click


def init():
    openBrowser()
    loginCGV()
    findMOIVE()
    checkTime()
    selectSeat()
#     closePopup()


init()
