

from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

# seek 채용 사이트
html = urlopen("https://www.seek.com.au/jobs")

bsObject = BeautifulSoup(html, "html.parser")

emp_link_data = bsObject.find_all('a', class_="_1tmgvw5 _1tmgvw7 _1tmgvwa _1tmgvwb _1tmgvwe yvsb870 yvsb87f _14uh994h")

# 채용 사이트 링크
emp_link = []
# 위치, 직무, 시간
emp_info_all = []

# 채용 사이트 링크 emp_link에 넣기
for data in emp_link_data:
    emp_link.append(data.attrs['href'])

# 채용 사이트에 하나씩 방문해서 해당 채용 공고 정보 받아오기
for el in emp_link:
    el_front = 'https://www.seek.com.au'
    html = urlopen(el_front+el)

    bsObject = BeautifulSoup(html, "html.parser")

    data_all = bsObject.find_all('span', class_="yvsb870 _14uh9944u _1cshjhy0 _1cshjhy1 _1cshjhy21 _1d0g9qk4 _1cshjhya")

    emp_info = []
    for data in data_all:
        print(data.text)
    print('---------------------------------')