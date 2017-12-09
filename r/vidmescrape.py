import os
from urllib.request import urlopen as ureq
import subprocess as cmdd
from bs4 import BeautifulSoup as bs
my_url = 'https://vid.me/users'
uclient = ureq(my_url)
page_html = uclient.read()
uclient.close()
page_soup =  bs(page_html, "html.parser")
list = page_soup.find_all("div",{"class":"user_photo"})
i = 0 
#while i <= len(list):
 
for user in list:
    newpath = str(user.a["href"])
    path = newpath.replace("https://vid.me/", "")
    os.makedirs(path)
    os.chdir(path)
    cmdd.run(["youtube-dl", user.a["href"]])
    os.chdir("..")

    
    
