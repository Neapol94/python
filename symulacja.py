import sqlite3
import random
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



def getAllTeamsId():
    cur.execute("select count(id) from teams")
    ids = []
    for i in range(1, (cur.fetchone()[-1] + 1)):
        ids.append(i)
    return ids

def drawTeamsPairs(idList):

    pary = []
    i = 0
    random.shuffle(idList)
    while len(pary) < len(idList) // 2:
        pary.append(str(idList[i]) + " " + str(idList[i + 1]))
        i += 2
    return pary

def separateTeamsString(string):
    teams = string.split(" ")
    homeTeamId = teams[0]
    awayTeamId = teams[1]
    return homeTeamId, awayTeamId

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
    betterTeam = worseTeam = winnerProb = None
    thp = teamHome.potential + 1
    tap = teamAway.potential - 1
    if (thp == tap):
        thp  += 1
        betterTeam = teamHome
        worseTeam = teamAway

    if (thp  > tap):
        winnerProb = thp  - tap + 50  # percentage chance for a win
        betterTeam = teamHome
        worseTeam = teamAway
    elif(thp  < tap):
        winnerProb = tap - thp + 50  # percentage chance for a win
        betterTeam = teamAway
        worseTeam = teamHome
    return winnerProb, betterTeam, worseTeam



def betterTeamScore(winnerProb):
    betterTeamScoreProb = []

    betterTeamScoreFive = winnerProb // 18 * 10
    for i in range(int(betterTeamScoreFive)):
        betterTeamScoreProb.append(5)

    betterTeamScoreZero = (100 - winnerProb) // 7 * 10
    for i in range(int(betterTeamScoreZero)):
        betterTeamScoreProb.append(0)

    betterTeamScoreFour = winnerProb // 10 * 10
    for i in range(int(betterTeamScoreFour)):
        betterTeamScoreProb.append(4)

    betterTeamScoreOne = (100 - winnerProb) // 8 * 10
    for i in range(betterTeamScoreOne):
        betterTeamScoreProb.append(1)

    betterTeamScoreThree = winnerProb // 5 * 10
    for i in range(int(betterTeamScoreThree)):
        betterTeamScoreProb.append(3)

    betterTeamScoreTwo = (100 - winnerProb) // 3 * 10
    for i in range(betterTeamScoreTwo):
        betterTeamScoreProb.append(2)

    return random.choice(betterTeamScoreProb)


def worseTeamScore(winnerProb):
    worseTeamScoreProb = []

    worseTeamScoreFive = (100 - winnerProb) // 30 * 10
    for i in range(worseTeamScoreFive):
        worseTeamScoreProb.append(5)

    worseTeamScoreFour = (100 - winnerProb) // 20 * 10
    for i in range(worseTeamScoreFour):
        worseTeamScoreProb.append(4)

    worseTeamScoreThree = (100 - winnerProb) // 10 * 10
    for i in range(int(worseTeamScoreThree)):
        worseTeamScoreProb.append(3)

    worseTeamScoreTwo = (100 - winnerProb) // 5 * 10
    for i in range(int(worseTeamScoreTwo)):
        worseTeamScoreProb.append(2)

    worseTeamScoreOne = winnerProb // 3 * 10
    for i in range(worseTeamScoreOne):
        worseTeamScoreProb.append(1)

    worseTeamScoreZero = winnerProb // 2 * 10
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


def roundResults(pairs):
    currentRound = []
    nextRound = []
    i = 1
    n = "\n"


    for pair in pairs:
        teamsPair = separateTeamsString(pair)
        homeTeamObject = teamCreate(int(teamsPair[0]))
        awayTeamObject = teamCreate(int(teamsPair[1]))
        winnerProb = winnerProbability(homeTeamObject, awayTeamObject)
        theResult = result(homeTeamObject, awayTeamObject, betterTeamScore(winnerProb[0]), worseTeamScore(winnerProb[0]))
        if (theResult[1] > theResult[2]):
            nextRound.append(homeTeamObject.id)
            currentRound.append(f"{i}: {theResult[0].name} {theResult[1]} - {theResult[2]} {theResult[3].name}")
        elif (theResult[1] < theResult[2]):
            nextRound.append(awayTeamObject.id)
            currentRound.append(f"{i}: {theResult[0].name} {theResult[1]} - {theResult[2]} {theResult[3].name}")
        elif(theResult[1] == theResult[2]):
            nextRound.append(theResult[0].id)
            currentRound.append(f"{i} {theResult[0].name} k: {theResult[1]} - {theResult[2]} {theResult[3].name}")

        i += 1
    return nextRound, currentRound


def saveScoreQuery(teamHomePotential, teamHomeScore, teamHomeConcede, teamHomePoints, winner):
    cur.execute("UPDATE teams set potential = ?, goals_scored = ?, goals_against = ?, points = ?"
                "where id = ?", (teamHomePotential, teamHomeScore, teamHomeConcede, teamHomePoints, winner))

def saveScores(teamHome, teamHomeScore, teamAwayScore, teamAway):
    try:
        score = str(teamHomeScore) + "-" + str(teamAwayScore)
        #save match
        cur.execute("INSERT into matches values(?, ?, ?, ?, ?)", (None, dateGen(), score, teamHome.id, teamAway.id))

        # save both teams info update
        winner = 0
        if(teamHomeScore>teamAwayScore):
            winner = teamHome.id
            saveScoreQuery(teamHome.potential + 1, teamHome.goals_scored + teamHomeScore,
                            teamHome.goals_against - teamAwayScore, teamHome.points + 3, winner)

            saveScoreQuery(teamAway.potential - 1, teamAway.goals_scored + teamAwayScore,
                                         teamAway.goals_against - teamHomeScore, teamAway.points + 0, teamAway.id)
        elif(teamHomeScore<teamAwayScore):
            winner = teamAway.id
            saveScoreQuery(teamAway.potential + 1, teamAway.goals_scored + teamAwayScore,
                                         teamAway.goals_against - teamHomeScore, teamAway.points + 3, winner)

            saveScoreQuery(teamHome.potential - 1, teamHome.goals_scored + teamHomeScore,
                            teamHome.goals_against - teamAwayScore, teamHome.points + 0, teamHome.id)
        else:
            saveScoreQuery(teamAway.potential + 0, teamAway.goals_scored + teamAwayScore,
                                         teamAway.goals_against - teamHomeScore, teamAway.points + 1, teamAway.id)

            saveScoreQuery(teamHome.potential + 0, teamHome.goals_scored + teamHomeScore,
                                         teamHome.goals_against - teamAwayScore, teamHome.points + 1, teamHome.id)
    except Error as e:
        print(e)

def cupSimulation(pairs):
    lastSixteenResults = roundResults(pairs)
    quarterfinalResults = roundResults(drawTeamsPairs(lastSixteenResults[0]))
    semifinalResults = roundResults(drawTeamsPairs(quarterfinalResults[0]))
    finalResults = roundResults(drawTeamsPairs(semifinalResults[0]))
    return finalResults[1]



# homeId = getTeamId()
# awayId = getTeamId()
#
# team = teamCompare(homeId, awayId)
# teamHomeObject = teamCreate(team[0])
# teamAwayObject = teamCreate(team[1])
#
# probability = winnerProbability(teamHomeObject, teamAwayObject)
# bts = betterTeamScore(probability)
# wts = worseTeamScore(probability)
#
#
# print(result(teamHomeObject, teamAwayObject, bts, wts)[0].name, result(teamHomeObject, teamAwayObject, bts, wts)[1],
#       result(teamHomeObject, teamAwayObject, bts, wts)[2], result(teamHomeObject, teamAwayObject, bts, wts)[3].name)
#
#
#
# saveScores(result(teamHomeObject, teamAwayObject, bts, wts)[0], result(teamHomeObject, teamAwayObject, bts, wts)[1],
#            result(teamHomeObject, teamAwayObject, bts, wts)[2], result(teamHomeObject, teamAwayObject, bts, wts)[3])

# para = 0
#
# lastSixteenResults = roundResults(drawTeamsPairs(getAllTeamsId()))
#
# # for i in lastSixteenResults[0]:
# #     print(i)
# print("Last 16: ")
# for i in lastSixteenResults[1]:
#     print(i)
#
# quarterfinalResults = roundResults(drawTeamsPairs(lastSixteenResults[0]))
#
# # for i in quarterfinalResults[0]:
# #     print(i)
# print("Quarterfinals: ")
# for i in quarterfinalResults[1]:
#     print(i)
#
# semifinalResults = roundResults(drawTeamsPairs(quarterfinalResults[0]))
#
# # for i in semifinalResults[0]:
# #     print(i)
# print("Semifinals: ")
# for i in semifinalResults[1]:
#     print(i)
#
# finalResults = roundResults(drawTeamsPairs(semifinalResults[0]))
#
# # for i in semifinalResults[0]:
# #     print(i)
# print("Final: ")
# for i in finalResults[1]:
#     print(i)

pairs = drawTeamsPairs(getAllTeamsId())
print(cupSimulation(pairs))

# lastSixteenResult = roundResults(drawTeamsPairs(getAllTeamsId()))[0]
# print("Quarterfinal")
# for i in roundResults(drawTeamsPairs(lastSixteenResult))[1]:
#     print(i)

con.commit()
con.close()
