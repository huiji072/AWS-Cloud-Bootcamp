import datetime
import re
from sched import scheduler
from urllib.request import urlopen
import numpy
import pandas
from bs4 import BeautifulSoup
import logging
logging.basicConfig(level=logging.DEBUG)
from slack_sdk import WebClient
import os
from dotenv import load_dotenv
import schedule

load_dotenv()

def Msg_bot():
    # 채널 토큰
    slack_token = os.environ.get("SLACK_TOKEN")
    # 채널명
    channel = '#seek'

    client = WebClient(token=slack_token)
    # 슬랙에 전송할 메세지 형식
    client.chat_postMessage(

        channel=channel, 
        blocks= [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": 
                    "스케줄러 테스트\n " 
			}
		},
        {
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": 
                    str(datetime.datetime.now())
			}
		}
	]
)

Msg_bot()

# schedule.every(10).seconds.do(Msg_bot())
