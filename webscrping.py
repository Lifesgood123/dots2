from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as bs
my_url = 'https://imgur.com/gallery/yyxSE'
uclient = ureq(my_url)
page_html = uclient.read()
uclient.close()
page_soup =  bs(page_html, "html.parser")
images = page_soup.findAll("div",{"class":"post-image"})
source_list = []
i = 0
for image in images:
    source = image.a["href"]
    source_list.append(source)
    print(source_list[i])
    i = i + 1
