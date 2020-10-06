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

    if(teams[0] != teams[1]):
        cur.execute("SELECT * FROM teams WHERE id in(?, ?)", (teams[0], teams[1],))
        team = cur.fetchall() #team[0] - gospodarz, team[1] - gość

        host = Team(None, team[0]['name'], team[0]['potential'], team[0]['stadium'], team[0]['symbol'], team[0]['league'],
            team[0]['points'], team[0]['goals_scored'], team[0]['goals_against'], team[0]['form'])
        visitor = Team(None, team[1]['name'], team[1]['potential'], team[1]['stadium'], team[1]['symbol'], team[1]['league'],
            team[1]['points'], team[1]['goals_scored'], team[1]['goals_against'], team[1]['form'])
        return host, visitor
    else:
        if (teams[0] == teams[1] and teams[0] == 1):
            teams[1] = teams[1] + 1
        elif (teams[0] == teams[1] and teams[0] == cur.fetchone()[-1]):
            teams[1] = teams[1] - 1


def match(teamHome, teamAway):
    def betterTeam(): #which team is better
        teamHome.potential += 1
        if(teamHome.potential>teamAway.potential): return teamHome
        elif(teamHome.potential == teamAway.potential):
            teamHome.potential +=1
            return teamHome
        else: return teamAway
    def worseTeam(): #which team is worse
        teamAway.potential -= 1
        if(teamHome.potential>teamAway.potential): return teamAway
        elif (teamHome.potential == teamAway.potential):
            teamAway.potential -= 1
            return teamAway
        else: return teamHome

    winnerProb = betterTeam().potential - worseTeam().potential + 50 #percentage chance for a win

    def result():

        betterTeamScoreProb = []
        adv = betterTeam().potential - worseTeam().potential #advantage
        #totalProb = (adv/5 + adv/4 + adv/3 + adv/2 + adv/1) * 10 #podstawa

        betterTeamScoreFive = (betterTeam().potential - worseTeam().potential)
        for i in range(int(betterTeamScoreFive)):
            betterTeamScoreProb.append(5)


        betterTeamScoreZero = (betterTeam().potential - worseTeam().potential)
        for i in range(int(betterTeamScoreZero)):
            betterTeamScoreProb.append(0)

        betterTeamScoreFour = (betterTeam().potential - worseTeam().potential) // 3.5 * 10
        for i in range(int(betterTeamScoreFour)):
            betterTeamScoreProb.append(4)

        betterTeamScoreOne = (betterTeam().potential - worseTeam().potential) // 3 * 10
        for i in range(betterTeamScoreOne):
            betterTeamScoreProb.append(1)

        betterTeamScoreThree = (betterTeam().potential - worseTeam().potential) // 1.5 * 10
        for i in range(int(betterTeamScoreThree)):
            betterTeamScoreProb.append(3)

        betterTeamScoreTwo = (betterTeam().potential - worseTeam().potential) // 1 * 10
        for i in range(betterTeamScoreTwo):
            betterTeamScoreProb.append(2)


        #worse team
        worseTeamScoreProb = []
        # totalProb = (adv/5 + adv/4 + adv/3 + adv/2 + adv/1) * 10 #podstawa

        worseTeamScoreFive = (betterTeam().potential - worseTeam().potential) // 6
        for i in range(worseTeamScoreFive):
            worseTeamScoreProb.append(5)

        worseTeamScoreFour = (betterTeam().potential - worseTeam().potential) // 5
        for i in range(worseTeamScoreFour):
            worseTeamScoreProb.append(4)

        worseTeamScoreThree = (betterTeam().potential - worseTeam().potential) // 4.5 * 10
        for i in range(int(worseTeamScoreThree)):
            worseTeamScoreProb.append(3)

        worseTeamScoreTwo = (betterTeam().potential - worseTeam().potential) // 3.5 * 10
        for i in range(int(worseTeamScoreTwo)):
            worseTeamScoreProb.append(2)

        worseTeamScoreOne = (betterTeam().potential - worseTeam().potential) // 2 * 10
        for i in range(worseTeamScoreOne):
            worseTeamScoreProb.append(1)

        worseTeamScoreZero = (betterTeam().potential - worseTeam().potential) // 2 // 5 * 10
        for i in range(worseTeamScoreZero):
            worseTeamScoreProb.append(0)

        if(teamHome.name==betterTeam().name):
            return print("Result is: \n" + betterTeam().name + " " + str(random.choice(betterTeamScoreProb))+ " - "
                        + str(random.choice(worseTeamScoreProb))+ " " + worseTeam().name)
        else:
            return print("Result is: \n" + worseTeam().name + " " + str(random.choice(worseTeamScoreProb)) + " - "
                         + str(random.choice(betterTeamScoreProb)) + " " + betterTeam().name)




    prc_chance_for_win = 'Match between ' + teamHome.name + ' home and ' + teamAway.name + ' away.\n' \
                         + '%s has %d%% chance to win this match' % (betterTeam().name, winnerProb)
    return print(prc_chance_for_win + "\n"), result()



match(twoTeams()[0], twoTeams()[1])