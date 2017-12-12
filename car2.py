#!/usr/bin/python
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as bs
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#setting up sheets api
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(creds)


#get Price search criteria from user
sheet = client.open("Craigslist cars").sheet1
max_price = "&max_price=" + input("max price? >  ")
min_price = "&min_price=" + input("min price? >  ")
##############################################################
#Contruct list of results
# Honestly there might be a more efficient way to do this, because 
# at the moment it holds it in ram and isn't efficient. Might be a better way to do this

def get_list(page):
    my_url = 'https://winstonsalem.craigslist.org/search/cta?s=' + str(page) + max_price + min_price
    uclient = ureq(my_url)
    page_html = uclient.read()
    uclient.close()
    page_soup =  bs(page_html, "html.parser")
    result = page_soup.find("ul", {"class":"rows"})
    return result

cars = []
page = 0
for i in range(0, 9): 
    stuff = get_list(page).findAll("li", {"class":"result-row"})
    for car in stuff:
        cars.append(car)
    page += 120

# The above for loop actually  makes the list.
###############################################################

print(len(cars))

rowcounter = 2
# Adding each list item to spreadsheet. 
for i in cars:
    postlink = i.p.a.get("href")
    postclient = ureq(postlink)
    post_html = postclient.read()
    postclient.close()
    post_soup = bs(post_html, "html.parser")
    attributes = post_soup.findAll("p", {"class":"attrgroup"})
    print(attributes[1].get_text())
    title = i.p.a.text
    holdup = i.p.findAll("span", {"class":"result-price"})
    sheet.update_cell(rowcounter, 1, title)

# Not all items have a price listed, so this for loop checks the length of the holdup list 

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
    
    # Print For debugging

    print("\n")
    print(title)
    print(price)
    print(hyper_link)
    print("\n")
