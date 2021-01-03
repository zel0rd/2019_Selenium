# !pip install requests-html
# import sys
import time
from selenium import webdriver
from requests_html import HTMLSession
from selenium.webdriver.chrome.options import Options

WEBDRIVER = webdriver.Chrome('./../Chrome_Driver/chromedriver')
WEBDRIVER_PATH = './../Chrome_Driver/chromedriver'

def get_movie_reviews(url, page_num=10):
    wd = WEBDRIVER
    wd.get(url)

    writer_list = []
    comment_list = []
    day_list = []

    for page_no in range(1, page_num+1):
        page_ul = wd.find_element_by_id('paging_point')
        page_a = page_ul.find_element_by_link_text(str(page_no))
        page_a.click()
        time.sleep(1)

        writers = wd.find_elements_by_class_name('writer-name')
        writer_list += [writer.text for writer in writers]

        comments = wd.find_elements_by_class_name('box-comment')
        comment_list += [comment.text for comment in comments]
        
        days = wd.find_elements_by_class_name('day')
        day_list += [day.text for day in days]

    # print(writer_list, len(writer_list))
    # print(comment_list, len(comment_list))
    # print(day_list, len(day_list))

    reviews = {"writer":writer_list, "comment":comment_list, "day":day_list}
    for i in range(len(reviews['writer'])):
        print("[{}] {} <{}>".format(reviews['writer'][i],reviews['comment'][i],reviews['day'][i]))

url = "http://www.cgv.co.kr/movies/detail-view/?midx=83327"
get_movie_reviews(url,10)