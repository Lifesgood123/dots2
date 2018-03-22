#!/usr/bin/env python3
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
        self.player_name_label = tkinter.StringVar()
        self.player_wins_label = tkinter.StringVar()
        self.player_losses_label = tkinter.StringVar()
        self.player_ties_label = tkinter.StringVar()
        self.player_skill_label = tkinter.StringVar()
        self.roles_label = tkinter.StringVar()
        self.player_role_1_label = tkinter.StringVar()
        self.player_role_2_label = tkinter.StringVar()
        self.player_role_3_label = tkinter.StringVar()
        roles_label = tkinter.Label(self, textvariable=self.roles_label, anchor="w")
        player_name_label = tkinter.Label(self, textvariable=self.player_name_label, anchor='w')
        player_wins_label = tkinter.Label(self, textvariable=self.player_wins_label, anchor='w')
        player_losses_label = tkinter.Label(self, textvariable=self.player_losses_label, anchor='w')
        player_ties_label = tkinter.Label(self, textvariable=self.player_ties_label, anchor='w')
        player_skill_label = tkinter.Label(self, textvariable=self.player_skill_label, anchor='w')
        player_role_1_label = tkinter.Label(self, textvariable=self.player_role_1_label, anchor='w')
        player_role_2_label = tkinter.Label(self, textvariable=self.player_role_2_label, anchor='w')
        player_role_3_label = tkinter.Label(self, textvariable=self.player_role_3_label, anchor='w')


        roles_label.grid(row=6, column=0)
        player_name_label.grid(row=1, column=0)
        player_skill_label.grid(row=2, column=0)
        player_wins_label.grid(row=3, column=0)
        player_losses_label.grid(row=4, column=0)
        player_ties_label.grid(row=5, column=0)
        player_role_1_label.grid(rowspan=3, row=7, column=0)
        player_role_2_label.grid(rowspan=3, row=10, column=0)
        player_role_3_label.grid(rowspan=3, row=13, column=0)
        
        self.player_name = tkinter.StringVar()
        self.player_wins = tkinter.StringVar()
        self.player_losses = tkinter.StringVar()
        self.player_ties = tkinter.StringVar()
        self.player_skill = tkinter.StringVar()
        self.player_role_1 = tkinter.StringVar()
        self.player_role_2 = tkinter.StringVar()
        self.player_role_3 = tkinter.StringVar()


        player_name = tkinter.Label(self, textvariable=self.player_name, anchor='w')
        player_wins = tkinter.Label(self, textvariable=self.player_wins, anchor='w')
        player_losses = tkinter.Label(self, textvariable=self.player_losses, anchor='w')
        player_ties = tkinter.Label(self, textvariable=self.player_ties, anchor='w')
        player_skill = tkinter.Label(self, textvariable=self.player_skill, anchor='w')
        player_role_1 = tkinter.Label(self, textvariable=self.player_role_1, anchor='w')
        player_role_2 = tkinter.Label(self, textvariable=self.player_role_2, anchor='w')
        player_role_3 = tkinter.Label(self, textvariable=self.player_role_3, anchor='w')
        player_role_1.grid(row=7, column=1)
        player_role_2.grid(row=10, column=1)
        player_role_3.grid(row=13, column=1)
        player_name.grid(row=1, column=1)
        player_skill.grid(row=2, column=1)
        player_wins.grid(row=3, column=1)
        player_losses.grid(row=4, column=1)
        player_ties.grid(row=5, column=1)
        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, True)



    def OnPressEnter(self, event):
        self.player_name_label.set("Name:")
        self.player_wins_label.set("Wins")
        self.player_losses_label.set("Losses:")
        self.player_ties_label.set("ties:")
        self.player_skill_label.set("Skill:")
        info = self.get_info(self.entry.get())
        print(info)
        keys = list(info['Roles'].keys())
        self.player_role_1_label.set(keys[0])
        self.player_role_2_label.set(keys[1])
        self.player_role_3_label.set(keys[2])
        self.player_role_1.set(info['Roles'][keys[0]])
        self.player_role_2.set(info['Roles'][keys[1]])
        self.player_role_3.set(info['Roles'][keys[2]])
        self.player_name.set(info["name"])
        self.player_wins.set(info['wins'])
        self.player_losses.set(info['losses'])
        self.player_ties.set(info['ties'])
        self.player_skill.set(info['skill_rating'])



        


    def get_info(self, gametag):
        print("scraping")
        fuckfuckfuck = gametag
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
        try:
            record = care[3].find_all('span')
        except:
            backup = {
                    'wins':'Not Found',
                    'losses':'Not Found',
                    'ties':'Not Found',
                    'skill_rating':'Not Found'
                    }
            
            backup['name'] = self.entry.get()
            return backup
        player_info = {}
        try:
            player_info['wins'] = record[0].text
        except:
            player_info['wins'] = 'NULL'
        try:
            player_info['losses'] = record[2].text
        except:    
            
            player_info['losses'] = 'NULL'
        try:
            player_info['ties']= record[4].text
        except:    
            player_info['ties'] = 'NULL'
        try:
            player_info['skill_rating'] = care[1].dd.span.span.text
        except:
            player_info['skill_rating'] = 'NULL'
        bio = page_soup.find('div', {'class':'layout-header-primary-bio'})
        bio.small.extract()
        player_info['name'] = bio.h1.text.replace("\n", "" )
        roles = page_soup.find('tbody', {"class":"stripe-rows"})
        classes = roles.find_all('tr')
        player_info['Roles'] = {}
        for i in classes:
            yo = i.find_all("td") 
            player_info['Roles'][yo[1].a.text] = {
                "games played":yo[2].text,
                "Win Percentage":yo[3].text
            } 
        return player_info
"""
            ("my_url = 'https://www.overbuff.com/players/xbl/'+fuckfuckfuck.replace(' ', '%20')+'/heroes?mode=competitive'
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
"""

if __name__ == "__main__":
    app = overbuff(None)
    app.title("Overbuff")
    app.mainloop()























