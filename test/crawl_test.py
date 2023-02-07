from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

# url의 html 가져오기
html = urlopen("https://www.seek.com.au/job/59763580?cid=company-profile")

bsObject = BeautifulSoup(html, "html.parser")

data_all = bsObject.find_all('span', class_="yvsb870 _14uh9944u _1cshjhy0 _1cshjhy1 _1cshjhy21 _1d0g9qk4 _1cshjhya")

# 위치, 직무, 시간
emp_info = []

for data in data_all:
    emp_info.append(data.text)

print(emp_info[9:12])

company_name = bsObject.find('a', class_="yvsb870 yvsb87f _1csk0c34").text
print(company_name)
