import datetime
import re
from urllib.request import urlopen
import numpy
import pandas
from bs4 import BeautifulSoup
import logging
logging.basicConfig(level=logging.DEBUG)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def Msg_bot(link, company_name, locate, job, post):
    slack_token = 'xoxb-4577538761255-4666924670823-P9gcxT45qFeM97r3vA4WSivp'
    channel = '#seek'
    # message = slack_message
    client = WebClient(token=slack_token)
    client.chat_postMessage(

        channel=channel, 
        blocks= [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*SEEK 채용 공고*\n" + "*<" +link+ ">*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": 
                    "*회사명:*\n" + company_name + "\n"
                    "*위치:*\n" + locate + "\n"
                    "*직무:*\n" + job + "\n"
                    "*공고날짜:*\n" + post
                    
			}
		}
	]
)

emp_info_all = []
for pageNum in range(3):

    # seek 채용 사이트
    html = urlopen("https://www.seek.com.au/jobs?page=" + str(pageNum) )

    bsObject = BeautifulSoup(html, "html.parser")
        
    # 채용사이트에 개별 링크 가져오기
    emp_link_data = bsObject.find_all('a', class_="_1tmgvw5 _1tmgvw7 _1tmgvwa _1tmgvwb _1tmgvwe yvsb870 yvsb87f _14uh994h")

    # 채용 사이트 링크
    emp_link = []

    # 채용 사이트 링크 emp_link에 넣기
    for data in emp_link_data:
        emp_link.append(data.attrs['href'])

    # 채용 사이트에 하나씩 방문해서 해당 채용 공고 정보 받아오기
    for el in emp_link:

        el_front = 'https://www.seek.com.au'
        html = urlopen(el_front+el)

        # 개별 사이트 링크
        link = el_front+el

        bsObject = BeautifulSoup(html, "html.parser")

        # 회사명
        company_name = bsObject.find('span', class_="yvsb870 _14uh9944u _1cshjhy0 _1cshjhy2 _1cshjhy21 _1d0g9qk4 _1cshjhyd").text
        # print("회사명: ", company_name)

        # 채용 공고 가져오기
        data_all = bsObject.find_all('span', class_="yvsb870 _14uh9944u _1cshjhy0 _1cshjhy1 _1cshjhy21 _1d0g9qk4 _1cshjhya")

        # 가져온 채용 공고를 text 형식으로 emp_info에 넣기
        emp_info = []
        for data in data_all:
            emp_info.append(data.text)
            
        # 공고일
        post_all = bsObject.find_all('span', class_="yvsb870 _14uh9944u _1cshjhy0 _1cshjhy1 _1cshjhy22 _1d0g9qk4 _1cshjhya")
        post_ = 0
        # 마지막 값인 날짜만 받아오면 됨
        for pa in post_all:
            post_ = pa.text


        today = datetime.datetime.now().date()
        post = 0
        # h ago, m_ago이면 당일로 계산, d ago이면 오늘날짜 - day
        if 'h ago' in post_ or 'm ago' in post_:
            post = today
        elif 'd ago'in post_:
            numbers = re.sub(r'[^0-9]', '', post_) #숫자만 추출
            post = today - datetime.timedelta(int(numbers))



        # 링크마다 형식이 달라서 start, end 인덱스로 잡음
        start_index = 0
        for ei in emp_info:
            if(ei >= '0' and ei <= '9') and 'review' in ei:
                start_index = emp_info.index(ei)+1
                break
            else:
                start_index = emp_info.index('All SEEK products')+1
            

        # 위치
        locate = emp_info[start_index]
        # 직무
        job = emp_info[start_index+1]

        # 데이터에 [link, company_name, locate, job, today, post] 넣기
        emp_info_all.append([link, company_name, locate, job, str(today), str(post)])

    
numpy_emp_info_all = []
# 배열 -> numpy -
for eia in emp_info_all:
    numpy_emp_info_all.append(numpy.array(eia))
    Msg_bot(eia[0], eia[1], eia[2], eia[3], eia[5])

# DataFrame -> csv
df_emp_info_all = pandas.DataFrame(numpy_emp_info_all, columns=['link', 'companyName', 'locate', 'job', 'today', 'post'])
# df_emp_info_all.to_csv('/Users/kimhuiji/Documents/seek_csv/seek_data.csv')