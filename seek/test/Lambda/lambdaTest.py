# from bs4 import BeautifulSoup
import requests

def handler(event, context):
    response = requests.get('http://www.apache.org')
    parsedHtml = response.text
    # soup = BeautifulSoup(parsedHtml, 'html.parser')
    # print(soup.find_all('a'))



    