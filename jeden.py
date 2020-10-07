import sqlite3, random


con = sqlite3.connect('C:/sqlite/db/football.db')#db connection

con.row_factory = sqlite3.Row#columns access via indexes and names

cur = con.cursor()#creating cursor object

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


def getTeamId():
    cur.execute("select count(id) from teams")
    teamId = random.choice(range(1, (cur.fetchone()[-1] + 1)))

    return teamId


def teamsCompare(firstTeamId, secondTeamId):
    while(firstTeamId==secondTeamId):
        secondTeamId = random.choice(range(1, (cur.fetchone()[-1] + 1)))
    return firstTeamId, secondTeamId

def teamCreate(id):
    cur.execute("SELECT * FROM teams WHERE id = ?", (id,))
    team = cur.fetchall()

    teamObject = Team(team[0]['id'], team[0]['name'], team[0]['potential'], team[0]['stadium'],
                team[0]['symbol'], team[0]['league'], team[0]['points'],
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

def result(teamHome, teamAway, betterTeamScore, worseTeamScore):
    if(teamHome.potential>teamAway.potential):
        teamHomeScore = betterTeamScore
        teamAwayScore = worseTeamScore
    else:
        teamHomeScore = worseTeamScore
        teamAwayScore = betterTeamScore

    return print("%s %d - %d %s" % (teamHome.name, teamHomeScore, teamAwayScore, teamAway.name))

teamHome = teamCreate(getTeamId())
teamAway = teamCreate(getTeamId())
team = teamsCompare(teamHome, teamAway)


probability = winnerProbability(betterTeam(teamHome, teamAway)[0], betterTeam(teamHome, teamAway)[1])
bts = betterTeamScore(probability)
wts = worseTeamScore(probability)
result(teamHome, teamAway, bts, wts)

con.commit()
con.close()
