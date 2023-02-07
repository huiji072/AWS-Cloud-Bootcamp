# from bs4 import BeautifulSoup
import requests

def handler(event, context):
    response = requests.get('http://www.apache.org')
    parsedHtml = response.text
    # soup = BeautifulSoup(parsedHtml, 'html.parser')
    # print(soup.find_all('a'))



    
    # 데이터 잘  쌓ㅣㅏㄴ 더기x