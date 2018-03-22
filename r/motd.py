import feedparser
from time import sleep
url = 'http://hosted2.ap.org/atom/APDEFAULT/3d281c11a96b4ad082fe88aa0db04305'
feed = feedparser.parse(url)
for i in feed['items']:
    print(i['title'])
    sleep(3)
