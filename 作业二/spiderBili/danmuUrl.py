from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import time
from bs4 import BeautifulSoup

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver_1 = webdriver.Chrome('D:\\chromedriver.exe')

danmuUrl=[]
for value in range(412947952,412947952):
    time.sleep( 0.1 )
    driver_1.get("https://www.bilibili.com/video/av{}".format(value))
    html = driver_1.page_source
    cid = re.findall('https://cn-gdgz-fx-bcache-\d{2}.bilivideo.com/upgcxcode/\d{2}/\d{2}/\d{9}',html)

    ##判空
    if cid:
        cidNum = cid.pop()
        cidNum = cidNum[-9:]
        dm_url = 'https://api.bilibili.com/x/v1/dm/list.so?oid='+cidNum
        with open('D:\spiderBili\danmuUrl.txt', 'a',encoding='utf-8') as f:
            f.write(dm_url + '\n')