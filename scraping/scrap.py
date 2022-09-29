from urllib import request
from numpy import result_type
from  selenium import webdriver
from django.http import HttpResponse
from time import sleep
from bs4 import BeautifulSoup
import requests

# def WebScraping():
#     op = webdriver.ChromeOptions()
#     op.add_argument('headless')
#     driver = webdriver.Chrome(executable_path ='C:\\Users\\user\\Downloads\\chromedriver.exe',options = op)
#     driver.get('https://zeenews.india.com//latest-news')
#     hs =driver.find_elements_by_xpath('//div[contains(@class ,"sec-con-box")]')
#     cs = driver.find_elements_by_xpath('//div[contains(@class ,"sec-con-box")]/p')
#     headlines = [hs[i].text for i in range(len(hs))]
#     contents = [cs[i].text for i in range(len(cs))]
#     news = []
#     for i in range(len(headlines)):
#         news.append([headlines[i], contents[i]])

#     return news


# def QuotesScraping():
#     op = webdriver.ChromeOptions()
#     op.add_argument('headless')
#     driver = webdriver.Chrome(executable_path ='C:\\Users\\user\\Downloads\\chromedriver.exe',
#      options = op)
#     driver.get('https://www.inc.com/jayson-demers/51-quotes-to-inspire-success-in-your-life-and-business.html')
#     st = driver.find_elements_by_class_name('standardText')
#     quotes = []
#     for i in range(len(st)):
#         quotes.append(st[i].text)
#     return quotes

rs = requests.get('https://www.shopify.com/in/blog/motivational-quotes')
if str(rs.status_code).startswith('2'):
    html  = rs.text
    Data = BeautifulSoup(html,'html.parser')
    st = Data.find_all(class_ = 'long-form-content')
    q2 = st[0].find_all('p')[5:]
    q1 = st[0].find_all('li')
    quotes = []
    for i in range(len(q1)):
        quotes.append(q1[i].text)
    for i in range(len(q2)):
        quotes.append(q2[i].text)
    

def QuotesScrapingBs():
    if len(quotes)!=0:
        
        return quotes

    else:
        return " This Page is experiencing difficulties at the moment, Please check back soon."

rs = requests.get('https://timesofindia.indiatimes.com/briefs')
html  = rs.text
Data = BeautifulSoup(html,'html.parser')
toi = Data.find_all(class_ = 'brief_box')
news = []
for i in toi:
    if i.h2!=None:
        news.append([i.h2.text, i.p.text])
   
def WebScrapingBs():
     return news

    
   
