import feedparser
import os
#feed = feedparser.parse('https://fivethirtyeight.com/all/feed')
#feed = feedparser.parse('http://feeds.feedburner.com/linuxjournalcom')
feeds = {
        'Linux Journal':'http://feeds.feedburner.com/linuxjournalcom',
        'Five Thirty Eight':'http://fivethirtyeight.com/all/feed',
        'BBC News':'https://feeds.bbci.co.uk/news/rss.xml?edition=us'
        }
def feed_menu():
    feed_list = list(feeds.keys())
    for i in feed_list:
        print(str(feed_list.index(i))+") "+ i)
    feed_select = input('PICK FEED>>>  ')
    feed = feedparser.parse(feeds[feed_list[int(feed_select)]])

    for i in feed['entries']:
        i['read'] = 0
        print(i['title'])

    mainmenu(feed)

def mainmenu(feed):
    count = 0
    for i in feed['entries']:
        toprint = str(count)+') '+i['title']

#        if i['read'] == 0:
#            print(toprint+' [UNREAD)')
#        else:
#           print(toprint)
        print(toprint)
        count += 1 
    inputt = input("ARTICLE NUMBER>>>>  ")
    if inputt == 'b':
        feed_menu()    
    else:            
        read(feed, int(inputt))
    os.system('clear')

def read(feed, index):
    os.system('clear')
    title = feed['entries'][index]['title']
    print('Currently Reading\n'+title)
    dir_path = os.path.dirname(os.path.realpath(__file__)) 
    with open(dir_path+'/.reading.html', 'w') as f:
        f.truncate()
        f.write("""
            <html lang="en">
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="./style.css">
  <title>{}</title>
</head>
<div class="stuff">
<body>
<h1>{}</h1>
        """.format(title, title))
        try:
            f.write(feed['entries'][index]['content'][0]['value'])
        except:
            f.write(feed['entries'][index]['summary']) 
        f.write("""
        <p><a href='{}'>Probably Fulll article</a></p>
</body>
</div>
</html>
        """.format(feed['entries'][index]['links'][0]['href'])) 
    feed['entries'][index]['read'] = 1
    os.system('firefox ' + dir_path+ "/.reading.html")
    mainmenu(feed)

feed_menu()
