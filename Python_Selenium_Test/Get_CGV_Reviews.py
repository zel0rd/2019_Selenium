# import sys
import time
from selenium import webdriver
WEBDRIVER = webdriver.Chrome('./../Chrome_Driver/chromedriver')
url = "http://www.cgv.co.kr/movies/detail-view/?midx=83327"

def example():
    browser = WEBDRIVER
    browser.get("http://python.org")

    menus = browser.find_elements_by_css_selector('#top ul.menu li')
    
    pypi = None
    for m in menus:
        if m.text == "PyPI":
            pypi = m
        print(m.text)
    
    pypi.click()  # 클릭
    
    time.sleep(5) # 5초 대기
    browser.quit() # 브라우저 종료

def get_movie_reviews(url, page_num=10):
    wd = WEBDRIVER
    wd.get(url)

    writer_list = []
    comment_list = []

    for page_no in range(1, page_num+1):
        page_ul = wd.find_element_by_id('paging_point')
        page_a = page_ul.find_element_by_link_text(str(page_no))
        page_a.click()
        time.sleep(1)

        writers = wd.find_elements_by_class_name('writer-name')
        writer_list += [writer.text for writer in writers]

        comments = wd.find_elements_by_class_name('box-comment')
        comment_list += [comment.text for comment in comments]
        # print(writer_list)
        # print(comment_list)
    review = dict(zip(writer_list, comment_list))
    # print(review)

    for i, k in enumerate(review):
        # print(i," : ",k, review[k])
        print("[{}] {} : {}".format(i,k,review[k]))
get_movie_reviews(url,10)