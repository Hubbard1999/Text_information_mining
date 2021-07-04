from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import time
from bs4 import BeautifulSoup

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver_1 = webdriver.Chrome('D:\\chromedriver.exe')
driver_1.get("https://www.bilibili.com/video/BV1FV411d7u7")
html = driver_1.page_source

cid = re.findall('https://cn-gdgz-fx-bcache-\d{2}.bilivideo.com/upgcxcode/\d{2}/\d{2}/\d{9}',html)
cidNum = cid.pop()
cidNum = cidNum[-9:]
dm_url = 'https://api.bilibili.com/x/v1/dm/list.so?oid='+cidNum
print(dm_url)


driver_1.get(dm_url)
time.sleep(3)
html = driver_1.page_source
driver_1.close()
html = BeautifulSoup(html, "html.parser")
# print(html)
data = html.find('div', {'class':'opened'}).find_all('div', {'class':'line'})
data[1206].find_all('span')[-2].text
print(data)