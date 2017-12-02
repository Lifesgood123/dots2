from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as bs
my_url = 'https://en.wikipedia.org/wiki/Main_Page'
uclient = ureq(my_url)
page_html = uclient.read()
uclient.close()
page_soup =  bs(page_html, "html.parser")
featured = page_soup.body.p
arttext =  bs.get_text(page_soup.body.p, '\n')
print(arttext)

