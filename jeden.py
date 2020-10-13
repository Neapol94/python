import sqlite3, random
from sqlite3 import Error


con = sqlite3.connect('C:/sqlite/db/football.db')#db connection

con.row_factory = sqlite3.Row#columns access via indexes and names

cur = con.cursor()#creating cursor object

class Team:
  def __init__(self, id, name, potential, stadium, symbol, league, points, goals_scored, goals_against, form):
    self.id = id
    self.name = name
    self.potential = potential
    self.stadium = stadium
    self.symbol = symbol
    self.league = league
    self.points = points
    self.goals_scored = goals_scored
    self.goals_against = goals_against
    self.form = form


def getTeamId():
    cur.execute("select count(id) from teams")
    teamId = random.choice(range(1, (cur.fetchone()[-1] + 1)))

    return int(teamId)


def teamCreate(id):
    cur.execute("SELECT * FROM teams WHERE id = ?", (id,))
    team = cur.fetchall()

    teamObject = Team(team[0]['id'], team[0]['name'], team[0]['potential'], team[0]['stadium'],
                team[0]['symbol'], team[0]['league'], team[0]['points'],
                team[0]['goals_scored'], team[0]['goals_against'], team[0]['form'])
    return teamObject


def teamCompare(homeTeamId, awayTeamId):
    while(homeTeamId==awayTeamId):
        id = getTeamId()
        awayTeamId = id
    return homeTeamId, awayTeamId


def dateGen():
    def czyPrzestepny(rok):
        if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
            return True
        else:
            return False


    lata = ('2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020')
    rok = str(random.choice(lata))

    miesiace = []
    for i in range(1,13):
        if(i<10): miesiace.append("0"+ str(i))
        else: miesiace.append(str(i))
    miesiac = random.choice(miesiace)

    dzien = ""
    if(miesiac=="02"):
        if(czyPrzestepny(rok)):
            dzien = random.choice(range(1,30)) #luty 29dni
        else:
            dzien = random.choice(range(1, 29)) #luty 28dni
    if(miesiac in ['01', '03', '05', '07', '08', '10', '12']):
        dzien = random.choice(range(1, 32)) #31dniowe
    else: dzien = random.choice(range(1, 31)) #30dniowe

    if (dzien < 10): dzien = "0" + str(dzien)

    return rok + "-" + miesiac + "-" + str(dzien)



def winnerProbability(teamHome, teamAway):
    winnerProb = None
    thp = teamHome.potential + 1
    tap = teamAway.potential - 1
    if (thp == tap):
        thp  += 1

    if (thp  > tap):
        winnerProb = thp  - tap + 50  # percentage chance for a win
    elif(thp  < tap):
        winnerProb = tap - thp + 50  # percentage chance for a win
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

def result(teamHome, teamAway, betterTeamScore, worseTeamScore):
    if(teamHome.potential>teamAway.potential):
        teamHomeScore = betterTeamScore
        teamAwayScore = worseTeamScore
    else:
        teamHomeScore = worseTeamScore
        teamAwayScore = betterTeamScore

    return teamHome, teamHomeScore, teamAwayScore, teamAway


def saveScores(teamHome, teamHomeScore, teamAwayScore, teamAway):
    try:
        score = str(teamHomeScore) + "-" + str(teamAwayScore)
        #save match
        cur.execute("INSERT into matches values(?, ?, ?, ?, ?)", (None, dateGen(), score, teamHome.id, teamAway.id))

        # save both teams info update
        winner = 0
        if(teamHomeScore>teamAwayScore):
            winner = teamHome.id
            cur.execute("UPDATE teams set potential = ?, goals_scored = ?, goals_against = ?, points = ?"
                        "where id = ?",(teamHome.potential + 1, teamHome.goals_scored + teamHomeScore,
                            teamHome.goals_against - teamAwayScore, teamHome.points + 3, winner))
            cur.execute("UPDATE teams set potential = ?, goals_scored = ?, goals_against = ?, points = ?"
                        "where id = ?", (teamAway.potential - 1, teamAway.goals_scored + teamAwayScore,
                                         teamAway.goals_against - teamHomeScore, teamAway.points + 0, teamAway.id))
        elif(teamHomeScore<teamAwayScore):
            winner = teamAway.id
            cur.execute("UPDATE teams set potential = ?, goals_scored = ?, goals_against = ?, points = ?"
                        "where id = ?", (teamAway.potential + 1, teamAway.goals_scored + teamAwayScore,
                                         teamAway.goals_against - teamHomeScore, teamAway.points + 3, winner))
            cur.execute("UPDATE teams set potential = ?, goals_scored = ?, goals_against = ?, points = ?"
                        "where id = ?", (teamHome.potential - 1, teamHome.goals_scored + teamHomeScore,
                            teamHome.goals_against - teamAwayScore, teamHome.points + 0, teamHome.id))
        else:
            winner = 0
            cur.execute("UPDATE teams set potential = ?, goals_scored = ?, goals_against = ?, points = ?"
                        "where id = ?", (teamAway.potential + 0, teamAway.goals_scored + teamAwayScore,
                                         teamAway.goals_against - teamHomeScore, teamAway.points + 1, teamAway.id))
            cur.execute("UPDATE teams set potential = ?, goals_scored = ?, goals_against = ?, points = ?"
                        "where id = ?", (teamHome.potential + 0, teamHome.goals_scored + teamHomeScore,
                                         teamHome.goals_against - teamAwayScore, teamHome.points + 1, teamHome.id))
    except Error as e:
        print(e)





homeId = getTeamId()
awayId = getTeamId()

team = teamCompare(homeId, awayId)
teamHomeObject = teamCreate(team[0])
teamAwayObject = teamCreate(team[1])

probability = winnerProbability(teamHomeObject, teamAwayObject)
bts = betterTeamScore(probability)
wts = worseTeamScore(probability)


print(result(teamHomeObject, teamAwayObject, bts, wts)[0].name, result(teamHomeObject, teamAwayObject, bts, wts)[1],
      result(teamHomeObject, teamAwayObject, bts, wts)[2], result(teamHomeObject, teamAwayObject, bts, wts)[3].name)



saveScores(result(teamHomeObject, teamAwayObject, bts, wts)[0], result(teamHomeObject, teamAwayObject, bts, wts)[1],
           result(teamHomeObject, teamAwayObject, bts, wts)[2], result(teamHomeObject, teamAwayObject, bts, wts)[3])

con.commit()
con.close()
