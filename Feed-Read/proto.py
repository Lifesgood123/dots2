import feedparser
import os
feed = feedparser.parse('https://fivethirtyeight.com/all/feed')
count = 0

for i in feed['entries']:
    i['read'] = 0


def mainmenu():
    count = 0
    for i in feed['entries']:
        toprint = str(count)+') '+i['title']

        if i['read'] == 0:
            print(toprint+' [UNREAD)')
        count += 1 
    read(int(input("ARTICLE NUMBER>>>>  ")))

def read(index):
    title = feed['entries'][index]['title']
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
        f.write(feed['entries'][index]['content'][0]['value'])
        f.write("""
</body>
</div>
</html>
        """) 
    feed['entries'][index]['read'] = 1
    os.system('firefox ' + dir_path+ "/.reading.html")
    mainmenu()

mainmenu()
