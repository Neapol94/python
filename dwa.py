import sqlite3
import random

# utworzenie połączenia z bazą przechowywaną na dysku
# lub w pamięci (':memory:')
con = sqlite3.connect('C:/sqlite/db/football.db')

# dostęp do kolumn przez indeksy i przez nazwy
con.row_factory = sqlite3.Row

# utworzenie obiektu kursora
cur = con.cursor()


class Team:
    def __getitem__(self, name):
        self.name = name
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


def twoTeams(): #ma zwracać dwa obiekty

    cur.execute("select count(id) from teams")
    teams = random.sample(range(1, (cur.fetchone()[-1] + 1)), 2)

    teamValue0 = int(teams[0])
    teamValue1 = int(teams[1])

    if (teamValue0 == teamValue1):
        return print("takie same: " + teams[0]['name'], teams[1]['name'])
    elif (teamValue0 != teamValue1):
        cur.execute("SELECT * FROM teams WHERE id in(?, ?)", (teams[0], teams[1],))
        team = cur.fetchall()  # team[0] - gospodarz, team[1] - gość

        host = Team(None, team[0]['name'], team[0]['potential'], team[0]['stadium'], team[0]['symbol'],
                    team[0]['league'],
                    team[0]['points'], team[0]['goals_scored'], team[0]['goals_against'], team[0]['form'])
        visitor = Team(None, team[1]['name'], team[1]['potential'], team[1]['stadium'], team[1]['symbol'],
                       team[1]['league'],
                       team[1]['points'], team[1]['goals_scored'], team[1]['goals_against'], team[1]['form'])
        return host, visitor


def match(teamHome, teamAway):
    def betterTeam(): # betterTeam()[0] is better, betterTeam()[1] is worse
        teamHome.potential += 1
        teamAway.potential -= 1

        if(teamHome.potential>teamAway.potential): return teamHome, teamAway
        elif(teamHome.potential == teamAway.potential):
            teamHome.potential +=1
            return teamHome, teamAway
        else: return teamAway, teamHome

    winnerProb = betterTeam()[0].potential - betterTeam()[1].potential + 50 #percentage chance for a win

    def result():

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


        #worse team
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

        if(teamHome.name==betterTeam()[0].name):
            return random.choice(betterTeamScoreProb), random.choice(worseTeamScoreProb)
        else:
            return random.choice(worseTeamScoreProb), random.choice(betterTeamScoreProb)

    prc_chance_for_win = 'Match between ' + teamHome.name + ' home and ' + teamAway.name + ' away.\n' \
                         + '%s has %d%% chance to win this match' % (betterTeam()[0].name, winnerProb)
    return print("%s \n \n %s %d - %d %s" % (prc_chance_for_win, teamHome.name, result()[0], result()[1], teamAway.name))



match(twoTeams()[0], twoTeams()[1])
