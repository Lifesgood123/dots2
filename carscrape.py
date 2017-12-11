#!/usr/bin/python
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as bs
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#setting up sheets api
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(creds)

sheet = client.open("Craigslist cars").sheet1

my_url = 'https://winstonsalem.craigslist.org/search/sss?query=couches'
uclient = ureq(my_url)
page_html = uclient.read()
uclient.close()
page_soup =  bs(page_html, "html.parser")
result = page_soup.find("ul", {"class":"rows"})
cars = result.findAll("li", {"class":"result-row"})
rowcounter = 2
for i in cars:
	title = i.p.a.text
	holdup = i.p.findAll("span", {"class":"result-price"})
	sheet.update_cell(rowcounter, 1, title)
	if len(holdup) >= 1:
		price = holdup[0].text
	else:
		price = "Unknown"
	sheet.update_cell(rowcounter, 2, price)
	link = i.a.get("href")
	sheet.update_cell(rowcounter, 3, link)
	rowcounter += 1
	print("\n")
	print(title)
	print(price)
	print(link)
	print("\n")
