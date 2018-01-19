from selenium import webdriver
from bs4 import BeautifulSoup as bs
from pyperclip import copy
from os import system

url="http://allrecipes.com/search/results/?wt=stir%20fry&sort=re&page=2#2"
browser = webdriver.Firefox()
browser.get(url)
html = browser.page_source
soup = bs(html, "html.parser")
browser.close()
stuff=soup.findAll("article", {"class":"grid-col--fixed-tiles"})
head = 'http://allrecipes.com'
listt = []
links = []
for i in stuff:
    try:
        listt.append(i.h3.find("a").get('href'))
    except:
        continue
for i in listt:
    new = head + i
    links.append(new)

for i in links:
	copy(i)
	system("python recipe-scrapper")
