from bs4 import BeautifulSoup
import sqlite3
from requests import get

con = sqlite3.connect('C:/sqlite/db/football.db')#db connection
con.row_factory = sqlite3.Row#columns access via indexes and names
cur = con.cursor()#creating cursor object

URL = "https://www.skysports.com/premier-league-table"

page = get(URL)
bs = BeautifulSoup(page.content, "html.parser")

table = []
i=0
# for standing_table in bs.find_all('tbody', class_="standing-table__row"):
#
#     print(standing_table)
    #team = cell.find('a', class_="standing-table__cell--name-link",)
    #if(team != None):table.append(str(team.contents))

tbody = bs.find("tbody")
trs = tbody.find_all("tr", class_="standing-table__row")
tds = trs[0].find_all("td")
tabeleczka = []
for element in tds:
    tabeleczka.append(element.contents)
print(tabeleczka)




#cur.execute("INSERT into premier-league values(?, ?, ?, ?, ?)", (None, dateGen(), score, teamHome.id, teamAway.id))
#print(type(table[0]))