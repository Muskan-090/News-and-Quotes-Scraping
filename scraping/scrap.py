from numpy import result_type
from  selenium import webdriver
from django.http import HttpResponse
from time import sleep
from bs4 import BeautifulSoup
import requests

def WebScraping():
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(executable_path ='C:\\Users\\user\\Downloads\\chromedriver.exe',options = op)
    driver.get('https://zeenews.india.com/latest-news')
    hs =driver.find_elements_by_xpath('//div[contains(@class ,"sec-con-box")]')
    cs = driver.find_elements_by_xpath('//div[contains(@class ,"sec-con-box")]/p')
    headlines = [hs[i].text for i in range(len(hs))]
    contents = [cs[i].text for i in range(len(cs))]
    news = []
    for i in range(len(headlines)):
        news.append([headlines[i], contents[i]])

    return news


def QuotesScraping():
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(executable_path ='C:\\Users\\user\\Downloads\\chromedriver.exe',
     options = op)
    driver.get('https://www.inc.com/jayson-demers/51-quotes-to-inspire-success-in-your-life-and-business.html')
    st = driver.find_elements_by_class_name('standardText')
    quotes = []
    for i in range(len(st)):
        quotes.append(st[i].text)
    return quotes


# def WebScrapingBs():
#     rs = requests.get('https://zeenews.india.com/latest-news')
#     html  = rs.text
#     Data = BeautifulSoup(html,'html.parser')
#     zeenews =  Data.find_all(class_ = "sec-con-box")
#     news = []
#     for i in range(len(zeenews)):
#       news.append([zeenews[i].a.string,zeenews[i].p.string.strip('\n\t')])

#     return news








