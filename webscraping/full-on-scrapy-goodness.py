from selenium import webdriver
from bs4 import BeautifulSoup as bs
from pyperclip import paste
from sys import argv
def do_stuff(url):
	browser = webdriver.Firefox()
	browser.get(url)
	html = browser.page_source
	soup = bs(html, "html.parser")
	browser.close()
	title = soup.find("h1",{"class":"recipe-summary__h1"})
	file = open("../recipes/" + title.text,"w")
	print(title)
	ingrid = soup.findAll("li", {"class":"checkList__line"})
	for i in ingrid:
		if len(i.findAll("div", {"class":"offer-container"})) > 0:
			ingrid.pop(ingrid.index(i))
	directions = soup.find("ol",{"class":"list-numbers recipe-directions__list"})
	stuff = directions.findAll("li",{"class":"step"})
	for i in ingrid:
		try:
			new = i.text.replace('\n', '')
			new = new + '\n'
			print(new)
			file.write(new)
		except:
			print("meh")
	for i in stuff:
		try:
			new = i.text.replace('\n', '')
			new = new + '\n'
			print(new)
			file.write(new)

		except:
			print("meh")
def search():
	url="http://allrecipes.com/search/results/?wt="+ input("search terms> ") +"&sort=re&page=2#2"
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
		do_stuff(i)
search()