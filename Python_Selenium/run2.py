# !pip install requests-html
# import sys
import time
from selenium import webdriver
from requests_html import HTMLSession
from selenium.webdriver.chrome.options import Options

def example():
    browser =webdriver.Chrome('./gitignore/chromedriver.exe')
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
    wd =webdriver.Chrome('./gitignore/chromedriver.exe')
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

def get_post(url):
    url = "<$TARGET_URL>"

    options = Options()
    options.headless = True
    wd =webdriver.Chrome('./gitignore/chromedriver.exe',options= options)
    # browser = webdriver.Chrome(options=options)
    # browser.get(url)
    wd.get(url)
    time.sleep(5)

    # wd =webdriver.Chrome('./gitignore/chromedriver.exe')

    # writer_list = []
    # comment_list = []

    # for page_no in range(1000, 2000):
    #     wd.get(url+str(page_no))
    #     time.sleep(10)
    # time.sleep(5) # 시간을 어느 정도 충분히 주어야 합니다.
    
    # s = HTMLSession()
    # driver =webdriver.Chrome('./gitignore/chromedriver.exe')
    # cookies = driver.get_cookies()
    # driver.quit()
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'} # Selenium과 동일하게 맞춰주세요.
    # for cookie in cookies:
    #     c = {cookie['name']: cookie['value']} # 파이썬 2에서는 다른 방식으로 구현해야 된다고 알고 있습니다.
    #     s.cookies.update(c)
    # html = s.get(url, headers=headers)
    
    # print(html)

get_post(url)
# get_movie_reviews(url,10)