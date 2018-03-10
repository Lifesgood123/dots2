from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as bs
my_url = 'https://www.overbuff.com/players/xbl/Kind%20of%20Deaf?mode=competitive'
uclient = ureq(my_url)
page_html = uclient.read()
uclient.close()
page_soup =  bs(page_html, "html.parser")
stuff = page_soup.find('div', {'class':'layout-header-secondary'})
care = stuff.find_all('dl')
record = care[3].find_all('span')
wins = record[0].text
losses = record[2].text
ties = record[4].text
skill_rating = care[1].dd.span.span.text
print('''
wins = %s  losses = %s ties = %s SR = %s
''' % (wins, losses, ties, skill_rating))

