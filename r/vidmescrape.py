import os
from urllib.request import urlopen as ureq
from urllib.request import urlretrieve as uret
import subprocess as cmdd
from bs4 import BeautifulSoup as bs
my_url = 'https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-notes/'
uclient = ureq(my_url)
page_html = uclient.read()
uclient.close()
page_soup =  bs(page_html, "html.parser")
main = page_soup.find("main")
table = main.table
links = table.findAll("a", href=True)
os.chdir('../../Notes/')
count = 1
for i in links:
    name = str(count) + ' ' + i.text
    urlll = 'https://ocw.mit.edu' + i.get("href")
    os.makedirs('./' + name)
    os.chdir(name)
    uret(urlll, filename=name)
    count += 1
    os.chdir("../")

