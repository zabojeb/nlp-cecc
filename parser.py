import requests
from bs4 import BeautifulSoup

def parse(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    title = soup.find('span','topic-body__title').text
    text = soup.findAll('p','topic-body__content-text')
    page_text = ''
    for i in text:
        page_text += i.text + " "
    return {"title" : title, "text" : page_text}


