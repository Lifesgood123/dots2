from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as bs
my_url = 'https://en.wikipedia.org/wiki/Special:Random'
uclient = ureq(my_url)
page_html = uclient.read()
uclient.close()
page_soup =  bs(page_html, "html.parser")
summary = page_soup.body.p
title = bs.get_text(page_soup.h1)
arttext =  bs.get_text(page_soup.body.p)
print("""
        %s

        %s

        """ %(title, arttext))

