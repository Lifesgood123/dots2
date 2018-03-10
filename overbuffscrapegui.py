from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as bs
import tkinter


class overbuff(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        self.entry = tkinter.Entry(self)
        self.entry.grid(columnspan=3, column=0, row=0)
        self.entry.bind("<Return>", self.OnPressEnter)
        self.labelVarible = tkinter.StringVar()
        label = tkinter.Label(self, textvariable=self.labelVarible, anchor='w', bg='black', fg="white")
        label.grid(columnspan=6, rowspan=6, row=2, column=0)

        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, True)


    def OnPressEnter(self, event):
        print("Hi")

    

if __name__ == "__main__":
    app = overbuff(None)
    app.title("Overbuff")
    app.mainloop()


    


























"""(")
fuckfuckfuck = #holder code
my_url = 'https://www.overbuff.com/players/xbl/'+fuckfuckfuck.replace(' ', '%20')+'?mode=competitive'
try:
    uclient = ureq(my_url)
except:
    print("PLayer Not found")
    exit(127)   
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
print('wins = %s  losses = %s ties = %s SR = %s' % (wins, losses, ties, skill_rating))
if args.verbose:
    bio = page_soup.find('div', {'class':'layout-header-primary-bio'})
    bio.small.extract()
    name = bio.h1.text.replace("\n", "" )
    print('\n\n' + name, end="\n\n")
    roles = page_soup.find('tbody', {"class":"stripe-rows"})
    classes = roles.find_all('tr')
    print("\nSR = "+skill_rating+"\n")
    for i in classes:
        yo = i.find_all("td")
        for i in yo:
            if yo.index(i) == 0:
                continue 
            elif yo.index(i) == 1:
                print(i.a.text+": ", end=" ")
            elif yo.index(i) == 2:
                print("    Games Played: "+i.text, end=" ")
            elif yo.index(i) == 3:
                print("    Win Percentage: "+i.text)
            print("\n")
    my_url = 'https://www.overbuff.com/players/xbl/'+fuckfuckfuck.replace(' ', '%20')+'/heroes?mode=competitive'
    uclient = ureq(my_url)
    nonono = uclient.read()
    uclient.close()
    page_soup =  bs(nonono, "html.parser")
    kjasld = page_soup.find("tbody")
    rows = kjasld.find_all("tr")
    for i in rows:
        cols = i.find_all('td')
        print(cols[1].a.text, end='\n_________\n')
        print("Games PLayed "+cols[2].text)
        print("Win Rate: "+cols[3].text)
        print("On Fire:"+ cols[4].text)
        print('E:D = ' + cols[5].text)
        print("\n\n")
        #/  
    """