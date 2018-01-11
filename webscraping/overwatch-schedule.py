from selenium import webdriver
from bs4 import BeautifulSoup as bs

url = "https://overwatchleague.com/en-us/schedule"
browser = webdriver.Firefox()
browser.get(url)
html = browser.page_source
soup = bs(html, "html.parser")
schedule = soup.findAll("div", {"class":"ScheduleMatchList"})
browser.quit()
other_days = []
stuff = schedule[0].findAll("div", {"class":"MatchSchedule"})
for i in stuff:
	rows = i.findAll("div", {"class":"MatchRow MatchRow-match"})
	try:	
		header = i.find("div", {"class":"MatchRow-header MatchRow Date"})
		formup = header.findAll("span")
		date = (formup[0].text + ' ' +formup[1].text)
	except:
		header = i.find("span", {"class":"MatchRow-day"})
		date = header.text
	print(date)
	for i in rows:
		teams = i.findAll("div", {"class":"TeamLabel-name hidden-sm hidden-xs"})
		status = i.find("div", {"class":"MatchRow-status"})
		state = status.text
		team1 = teams[0].text
		team2 = teams[1].text
		
		print("""\t%s vs. %s
								%s""" % (team1, team2, state))
