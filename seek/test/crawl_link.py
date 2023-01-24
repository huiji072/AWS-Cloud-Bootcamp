from urllib.request import urlopen
import numpy
import pandas
from bs4 import BeautifulSoup
import logging
logging.basicConfig(level=logging.DEBUG)

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# slack_token = 'xoxb-4577538761255-4666924670823-P9gcxT45qFeM97r3vA4WSivp' # Bot OAuth Token
# client = WebClient(token=slack_token)

def Msg_bot(slack_message):
    slack_token = 'xoxb-4577538761255-4666924670823-P9gcxT45qFeM97r3vA4WSivp'
    channel = '#seek'
    message = slack_message
    client = WebClient(token=slack_token)
    client.chat_postMessage(channel=channel, text=message)

# seek 채용 사이트
html = urlopen("https://www.seek.com.au/jobs")

bsObject = BeautifulSoup(html, "html.parser")

# pagination 처리

    
# 채용사이트에 개별 링크 가져오기
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
    emp_data = []

    el_front = 'https://www.seek.com.au'
    html = urlopen(el_front+el)

    # 해당 사이트 emp_info_all에 넣기
    # emp_data[emp_url] = el_front+el
    # emp_info_all[emp_url] = el_front+el

    bsObject = BeautifulSoup(html, "html.parser")

    # 회사명
    company_name = bsObject.find('span', class_="yvsb870 _14uh9944u _1cshjhy0 _1cshjhy2 _1cshjhy21 _1d0g9qk4 _1cshjhyd").text
    # emp_info_all[emp_company_name] = company_name
    # emp_data[company_name] = company_name

    # 채용 공고 정보
    data_all = bsObject.find_all('span', class_="yvsb870 _14uh9944u _1cshjhy0 _1cshjhy1 _1cshjhy21 _1d0g9qk4 _1cshjhya")

    emp_info = []
    for data in data_all:
        emp_info.append(data.text)

    # 링크마다 형식이 달라서 start, end 인덱스로 잡음
    start_index = 0
    for ei in emp_info:
        if(ei >= '0' and ei <= '9') and 'review' in ei:
            start_index = emp_info.index(ei)+1
            break
        else:
            start_index = emp_info.index('All SEEK products')+1


    end_index = 0
    if 'More jobs from this company' in emp_info:
        end_index = emp_info.index('More jobs from this company')
    else:
        for ei in emp_info:
            if ei[0] == '$':
                end_index = emp_info.index(ei)

    # emp_info_all[2:4] = (emp_info[start_index-1:start_index+2])
    emp_info[start_index-1] = (company_name)
    # emp_data[emp_locate:emp_job+1] = emp_info[start_index-1:start_index+2]
    emp_info_all.append(emp_info[start_index-1:start_index+2])
    
numpy_emp_info_all = []
# 배열 -> numpy -> DataFrame -> csv파일에 저장
for eia in emp_info_all:
    numpy_emp_info_all.append(numpy.array(eia))
    for e in eia:
        Msg_bot(e)  

df_emp_info_all = pandas.DataFrame(numpy_emp_info_all, columns=['companyName', 'locate', 'job'])
# print(df_emp_info_all)
# df_emp_info_all.to_csv('/Users/kimhuiji/Documents/seek_csv/seek_data.csv')
