import unittest
from pprint import pprint
# # napis = "dopa"
# #
# # if napis == "dopa":
# #     print("To jest: %s" % napis)
#
# litery = ["A", "B", "C", "D", "E", "F", "G", "H"]
# cyfry = ["1", "2", "3", "4", "5", "6", "7", "8"]
# pola = []
# i=0
# j=0
#
# for i in range(len(litery)):
#
#     for j in range(len(cyfry)):
#         pola.append(litery[i]+cyfry[j])
#
#
#      #print(cyfry[i-1])
#
# print(pola)

# print(12/5/2*10)#score 0
# print(12/5/2*10)#score 5
# print(12/4*10)#score 4
# print(12/3*10)#score 1
# print(12/2*10)#score 3
# print(12/1*10) #score 2

#btsf = 17/5/2*10#score 5
# table = []
# for i in range(int(btsf)):
#     table.append(5)
# print(table)


import sqlite3, random

# utworzenie połączenia z bazą przechowywaną na dysku
# lub w pamięci (':memory:')
con = sqlite3.connect('C:/sqlite/db/football.db')

# dostęp do kolumn przez indeksy i przez nazwy
con.row_factory = sqlite3.Row

# utworzenie obiektu kursora
cur = con.cursor()

# cur.execute("""
#     CREATE TABLE IF NOT EXISTS teams (
#         id INTEGER PRIMARY KEY ASC,
#         name varchar(128) NOT NULL,
#         potential int(64),
#         stadium varchar(128) NOT NULL,
#         symbol varchar(32) NOT NULL,
#         league varchar(32) NOT NULL,
#         points int(32),
#         goals_scored int(64),
#         goals_against int(64),
#         form varchar(64) NOT NULL
#     )""")
# cur.executescript("""
#     CREATE TABLE IF NOT EXISTS matches (
#         id INTEGER PRIMARY KEY ASC,
#         date varchar(128) NOT NULL,
#         result varchar(64) NOT NULL,
#         home_team_id INTEGER NOT NULL,
#         away_team_id INTEGER NOT NULL,
#         FOREIGN KEY(home_team_id) REFERENCES teams(id),
#         FOREIGN KEY(away_team_id) REFERENCES teams(id)
#     )""")

# wstawiamy tuplę z czterema zespołami do dodania

# teams = (
#     (None, 'Brighton & Hove Albion', 33, 'Amex Stadium', 'BHA', 'Premier League', '0', '0', '0', ''),
#     (None, 'Aston Villa', 35, 'Villa Park', 'AVL', 'Premier League', '0', '0', '0', ''),
#     (None, 'Leicester', 41, 'King Power Stadium', 'LEI', 'Premier League', '0', '0', '0', ''),
#     (None, 'Southampton', 34, "Saint Mary Stadium", 'STH', 'Premier League', '0', '0', '0', ''),
# )
#podstawiamy tuplę do zapytania sql
# cur.executemany('INSERT INTO teams VALUES(?,?,?,?,?,?,?,?,?,?)', teams)

# wykonujemy zapytanie SQL, które pobierze id zespołu z tabeli "teams".
# cur.execute('SELECT id FROM teams WHERE symbol = ?', ('BHA',))
# home_team_id = cur.fetchone()[0]
# cur.execute('SELECT id FROM teams WHERE symbol = ?', ('AVL',))
# away_team_id = cur.fetchone()[0]

# # dodaję tuplę z danymi przykładowego meczu
# matches = (
#     ('2020-09-23', '3-1', home_team_id, away_team_id)
# )
# #print(type(matches[0]))
# cur.execute('INSERT INTO matches VALUES(NULL,?,?,?,?)', matches)



# def ktoWygral(homeTeam, awayTeam):
#     cur.execute(
#         """
#         SELECT matches.id,date,result,home_team_id,away_team_id,stadium,name FROM matches,teams
#         WHERE teams.id in (home_team_id, away_team_id)
#         """)
#     #pobiera dwa rzędy: 1 z gospodarzem a drugi z gościem
#     mecze = cur.fetchall()
#     wynik = mecze[0]['result'].split("-")
#     homeScore = wynik[0]
#     awayScore = wynik[1]
#     if(homeScore>awayScore):
#         return print("Dnia: " + mecze[0]['date'] + " mecz na stadionie " + mecze[0]['stadium'] + " wygrali gospodarze."
#                      "\n"+ mecze[0]['name']+ " " + homeScore + " - " + awayScore+ " " + mecze[1]['name'])
#     elif(homeScore<awayScore):
#         return print("Dnia: " + mecze[0]['date'] + " mecz na stadionie " + mecze[0]['stadium'] + " wygrali goście."+
#                      "\n"+ mecze[0]['name']+ " " + homeScore + " - " + awayScore+ " " + mecze[1]['name'])
#     else:
#         return print("Dnia: " + mecze[0]['date'] + " padł remis na stadionie " + mecze[0]['stadium'] +
#                      "\n"+ mecze[0]['name']+ " " + homeScore + " - " + awayScore+ " " + mecze[1]['name'])
#
#
# ktoWygral()

# teams = (
#     (None, 'Chelsea London', 44, 'Stamford Bridge', 'CHE', 'Premier League', '0', '0', '0', ''),
#     (None, 'Everton', 34, 'Goodison Park', 'EVE', 'Premier League', '0', '0', '0', ''),
#     (None, 'West Ham United', 30, 'The Olympic Stadium', 'WHU', 'Premier League', '0', '0', '0', ''),
#     (None, 'Liverpool', 48, "Anfield Road", 'LIV', 'Premier League', '0', '0', '0', ''),
#     (None, 'Manchester City', 45, "Etihad Stadium", 'MCI', 'Premier League', '0', '0', '0', ''),
#     (None, 'Sheffield United', 34, "Bramal Lane", 'SHU', 'Premier League', '0', '0', '0', ''),
#     (None, 'Wolverhampton Wanderers', 39, "Molineux Stadium", 'WOL', 'Premier League', '0', '0', '0', ''),
#     (None, 'Arsenal London', 40, "The Emirates", 'ARS', 'Premier League', '0', '0', '0', ''),
#     (None, 'Tottenham Hotspur', 41, "White Hart Lane", 'TOT', 'Premier League', '0', '0', '0', ''),
# )
# #podstawiamy tuplę do zapytania sql
# cur.executemany('INSERT INTO teams VALUES(?,?,?,?,?,?,?,?,?,?)', teams)



#print((35 - 23) // 2 * 2)
# cur.execute("select count(id) from teams")
# teams = random.sample(range(1,cur.fetchone()[-1]+1), 2)
# print(teams)
#
# cur.execute("SELECT * FROM teams WHERE id in(?, ?)", (teams[0],teams[1],))
# team = cur.fetchall()


# print(team1[0]['name'], team1[0]['potential'], team1[0]['stadium'], team1[0]['symbol'], team1[0]['league'], team1[0]['points'],
#       team1[0]['goals_scored'], team1[0]['goals_against'], team1[0]['form'])
class Team:
  def __init__(self, teamId, name, potential, stadium, symbol, league, points, goals_scored, goals_against, form):
    self.teamId = teamId
    self.name = name
    self.potential = potential
    self.stadium = stadium
    self.symbol = symbol
    self.league = league
    self.points = points
    self.goals_scored = goals_scored
    self.goals_scored = goals_against
    self.form = form


def getTwoTeamsId():
    cur.execute("select count(id) from teams")
    homeId = random.choice(range(1, (cur.fetchone()[-1] + 1)))
    awayId = random.choice(range(1, (cur.fetchone()[-1] + 1)))
    while(homeId==awayId):
        homeId = random.choice(range(1, (cur.fetchone()[-1] + 1)))

    return [homeId, awayId]


def teamCreate(id):
    cur.execute("SELECT * FROM teams WHERE id = ?", (id,))
    team = cur.fetchall()

    teamObject = Team(team[0]['id'], team[0]['name'], team[0]['potential'], team[0]['stadium'],
                team[0]['symbol'], team[0]['league'],team[0]['points'],
                team[0]['goals_scored'], team[0]['goals_against'], team[0]['form'])
    return teamObject


def betterTeam(teamHome, teamAway):
    teamHome.potential += 1
    teamAway.potential -= 1
    if (teamHome.potential > teamAway.potential):
        return teamHome, teamAway
    elif (teamHome.potential == teamAway.potential):
        teamHome.potential += 1
        return teamHome, teamAway
    else: return teamAway, teamHome #betterTeam, worseTeam


def winnerProbability(betterTeam, worseTeam):
    winnerProb = betterTeam.potential - worseTeam.potential + 50  # percentage chance for a win
    return winnerProb


def betterTeamScore(winnerProb):
    betterTeamScoreProb = []

    betterTeamScoreFive = winnerProb // 10 * 10
    for i in range(int(betterTeamScoreFive)):
        betterTeamScoreProb.append(5)

    betterTeamScoreZero = (100 - winnerProb) // 5 * 10
    for i in range(int(betterTeamScoreZero)):
        betterTeamScoreProb.append(0)

    betterTeamScoreFour = winnerProb // 5 * 10
    for i in range(int(betterTeamScoreFour)):
        betterTeamScoreProb.append(4)

    betterTeamScoreOne = (100 - winnerProb) // 4 * 10
    for i in range(betterTeamScoreOne):
        betterTeamScoreProb.append(1)

    betterTeamScoreThree = winnerProb // 3 * 10
    for i in range(int(betterTeamScoreThree)):
        betterTeamScoreProb.append(3)

    betterTeamScoreTwo = (100 - winnerProb) // 3 * 10
    for i in range(betterTeamScoreTwo):
        betterTeamScoreProb.append(2)

    return random.choice(betterTeamScoreProb)


def worseTeamScore(winnerProb):
    worseTeamScoreProb = []

    worseTeamScoreFive = (100 - winnerProb) // 10 * 10
    for i in range(worseTeamScoreFive):
        worseTeamScoreProb.append(5)

    worseTeamScoreFour = (100 - winnerProb) // 6 * 10
    for i in range(worseTeamScoreFour):
        worseTeamScoreProb.append(4)

    worseTeamScoreThree = (100 - winnerProb) // 4 * 10
    for i in range(int(worseTeamScoreThree)):
        worseTeamScoreProb.append(3)

    worseTeamScoreTwo = (100 - winnerProb) // 3 * 10
    for i in range(int(worseTeamScoreTwo)):
        worseTeamScoreProb.append(2)

    worseTeamScoreOne = winnerProb // 5 * 10
    for i in range(worseTeamScoreOne):
        worseTeamScoreProb.append(1)

    worseTeamScoreZero = winnerProb // 3 * 10
    for i in range(worseTeamScoreZero):
        worseTeamScoreProb.append(0)

    return random.choice(worseTeamScoreProb)


def result(teamHome, teamHomeScore, teamAway, teamAwayScore):
    return print("%s %d - %d %s" % (teamHome, teamHomeScore, teamAway, teamAwayScore))



con.commit()
con.close()
