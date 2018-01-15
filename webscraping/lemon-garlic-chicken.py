from selenium import webdriver
from bs4 import BeautifulSoup as bs

url = "http://allrecipes.com/recipe/18032/slow-cooker-lemon-garlic-chicken-ii/"
browser = webdriver.Firefox()
browser.get(url)
html = browser.page_source
soup = bs(html, "html.parser")
browser.close()
ingrid = soup.findAll("li", {"class":"checkList__line"})
for i in ingrid:
	if len(i.findAll("div", {"class":"offer-container"})) > 0:
		ingrid.pop(ingrid.index(i))
directions = soup.find("ol",{"class":"list-numbers recipe-directions__list"})
stuff = directions.findAll("li",{"class":"step"})
for i in ingrid:
	try:
		print(i.text)
	except:
		print("meh")
for i in directions:
	try:
		print(i.text)
	except:
		print("meh")

