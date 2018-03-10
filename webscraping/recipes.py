#!/usr/bin/pyhton
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("search_terms")
args = parser.parse_args()
print("searching for " + args.search_terms)


def do_stuff(url):
    browser = webdriver.Firefox()
    browser.get(url)
    html = browser.page_source
    soup = bs(html, "html.parser")
    browser.close()
    title = soup.find("h1", {"class": "recipe-summary__h1"})
    file = open("../recipes/" + title.text, "w")
    print(title)
    ingrid = soup.findAll("span", {"class": "recipe-ingred_txt added"})
    directions = soup.find("ol", {
        "class": "list-numbers recipe-directions__list"
    })
    stuff = directions.findAll("li", {"class": "step"})

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

    file.close()


def search():
    url = "http://allrecipes.com/search/results/?wt=" + args.search_terms + "&sort=re"
    browser = webdriver.Firefox()
    browser.get(url)
    html = browser.page_source
    soup = bs(html, "html.parser")
    browser.close()
    stuff = soup.findAll("article", {"class": "grid-col--fixed-tiles"})
    head = 'http://allrecipes.com'
    listt = []
    links = []

    for i in stuff:
        try:
            listt.append(i.h3.find("a").get('href'))
        except:
            continue

    print(listt)

    for i in listt:
        new = i
        links.append(new)
        print(links)
    for i in links:
        do_stuff(i)


search()
