import plotly.plotly as py
import plotly.graph_objs as go
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#setting up sheets api
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(creds)
dates = [] 
sheet = client.open(input("sheet name?")).sheet1
def setup_for_graphing(row, end_row, balance):
	for roww in range(row, end_row+1):
		transaction = sheet.cell(roww, 5).value
		try:
			tab = (float(transaction) * - 1)
			balance = (float(transaction) * -1) + balance
			print("- %s" % transaction)
		except:
			transaction = sheet.cell(roww, 4).value
			balance = float(transaction) + balance
			tab = float(transaction)
			print("+ %s" % transaction)
		sheet.update_cell(roww, 6, balance)
		sheet.update_cell(roww, 9, tab)
throwaway = sheet.col_values(1)
for days in throwaway:
	if days != '':
		dates.append(days)		
setup_for_graphing(1, len(dates), 250)
throwaway = sheet.col_values(1)
throwaway2 = sheet.col_values(6)
throwaway3 = sheet.col_values(9)

bal = []
tab = [] 
for monies in throwaway3:
	if monies != '':
		tab.append(float(monies))

for monies in throwaway2:
	if monies != '':
		bal.append(float(monies))

print(bal)
if len(dates) != len(bal):
	print(len(dates))
	print(len(bal))
count = 0 
count2 = len(dates)
while count <= count2:
	try:
		while dates[count] == dates[count + 1]:
			dates.pop(count+1)
			fuck = bal[count] - tab[count]
			fuck3 = bal[count] - fuck 
			bal[count] = fuck3 * -1
			bal.pop(count+1)
			fuck2 = tab[count] + tab[count + 1]
			tab[count] = fuck2
			tab.pop(count+1)
	except IndexError:
		print("Worked")
	except:
		print("I fucked up and I don't know where")
	count2 = len(dates)
	
	count = count + 1
count = 0 
count2 = len(dates)
 
print(dates)
print(bal)
print(tab)
print(len(tab))
print(len(bal))
print(len(dates))
date_number = []
date_numbers = []
for i in dates:
	sex = i.split('/')
	date_numbers.append(sex[1])
for i in date_numbers:
	date_number.append(int(i))

for i in range(0, len(date_number)):
	while int(date_number[i]) != int(date_number[i+1])-1:
		date_number.insert((i + 1), int(date_number[i+1]) - 1)
		bal.insert((i + 1), None)
new_date_numbers = []
new_dates = []

tired = dates[0].split('/')

for i in date_number:
	s = '/'
	new_date_numbers.append(s.join([tired[0], str(i), tired[2]]))
for i in new_date_numbers:
	new_dates.append(i)

trace0 = go.Scatter(
	x = new_dates,
	y = bal,
	name = 'November',
	connectgaps=True)
data = [trace0]
fig = dict(data=data)
py.plot(fig, filename='November')
