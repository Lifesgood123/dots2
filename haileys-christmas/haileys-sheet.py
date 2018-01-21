#!/usr/bin/python
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as bs
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from random import randint
import twittcher

#setting up sheets api
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(creds)


#get Price search criteria from user
sheet = client.open("Coupons").sheet1
chores = ['Clean the dishes', 'take out the dogs', 'take out the dogs', 'take out the dogs', 'take out the dogs', 'Clean living room', 'Clean Bedroom', 'Clean Bathroom', 'Clean Kitchen', 'Clean living room', 'Clean Bedroom', 'Clean Bathroom', 'Clean Kitchen', 'Clean living room', 'Clean Bedroom', 'Clean Bathroom', 'Clean Kitchen', 'backrub', 'knee rub', 'foot rub', 'Wildcard', 'backrub', 'knee rub', 'foot rub', 'Wildcard', 'backrub', 'knee rub', 'foot rub', 'Wildcard', 'backrub', 'knee rub', 'foot rub', 'Wildcard']
def reset():
	row = 1
	for i in chores:
		sheet.update_cell(row, 1, i)
		sheet.update_cell(row, 2, row)
		sheet.update_cell(row, 3, 'NO')
		row = row + 1
def use(key):
	keys = sheet.col_values(2)
	row = keys.index(key) + 1

def check():

