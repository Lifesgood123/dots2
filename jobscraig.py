#!/usr/bin/python
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as bs
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#setting up sheets api
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(creds)

sheet = client.open("Craig Jobs").sheet1
def get_list(page):
    my_url = 'https://winstonsalem.craigslist.org/d/jobs/search/jjj?s=0' + str(page) 
    uclient = ureq(my_url)
    page_html = uclient.read()
    uclient.close()
    page_soup =  bs(page_html, "html.parser")
    result = page_soup.find("ul", {"class":"rows"})
    return result
cars = []
for i in range(0, 9):
    page = 0 
    stuff = get_list(page).findAll("li", {"class":"result-row"})
    for car in stuff:
        cars.append(car)
    page += 120
print(len(cars))
rowcounter = 2
for i in cars:
    postlink = i.p.a.get("href")
    postclient = ureq(postlink)
    post_html = postclient.read()
    postclient.close()
    post_soup = bs(post_html, "html.parser")
    attributes = post_soup.findAll("p", {"class":"attrgroup"})
    if len(attributes) > 0:
        print(attributes[0].get_text())
    title = i.p.a.text
    holdup = i.p.findAll("span", {"class":"result-price"})
    sheet.update_cell(rowcounter, 1, title)
    if len(holdup) >= 1:
        price = holdup[0].text
    else:
        price = "Unknown"
    sheet.update_cell(rowcounter, 2, price)
    hyper_link = i.a.get("href")
    sheet.update_cell(rowcounter, 3, hyper_link)
    dayoftheyear = i.p.time.get("datetime")
    sheet.update_cell(rowcounter, 4, dayoftheyear)
    rowcounter += 1
    print("\n")
    print(title)
    print(price)
    print(hyper_link)
    print("\n")
