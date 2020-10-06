import sqlite3

# utworzenie połączenia z bazą przechowywaną na dysku
# lub w pamięci (':memory:')
con = sqlite3.connect('C:/sqlite/db/football.db')

# dostęp do kolumn przez indeksy i przez nazwy
con.row_factory = sqlite3.Row

# utworzenie obiektu kursora
cur = con.cursor()

import random
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
    teams = random.sample(range(1, cur.fetchone()[-1] + 1), 2)
    cur.execute("SELECT * FROM teams WHERE id in(?, ?)", (teams[0], teams[1],))
    team = cur.fetchall() #team[0] - gospodarz, team[1] - gość

    gospodarz = Team(None, team[0]['name'], team[0]['potential'], team[0]['stadium'], team[0]['symbol'], team[0]['league'],
        team[0]['points'], team[0]['goals_scored'], team[0]['goals_against'], team[0]['form'])
    gosc = Team(None, team[1]['name'], team[1]['potential'], team[1]['stadium'], team[1]['symbol'], team[1]['league'],
        team[1]['points'], team[1]['goals_scored'], team[1]['goals_against'], team[1]['form'])
    return gospodarz, gosc

def match(teamHome, teamAway):
    def better_team(): #which team is better
        teamHome.potential += 1
        if(teamHome.potential>teamAway.potential): return teamHome
        elif(teamHome.potential == teamAway.potential):
            teamHome.potential +=1
            return teamHome
        else: return teamAway
    def worse_team(): #which team is worse
        teamAway.potential -= 1
        if(teamHome.potential>teamAway.potential): return teamAway
        elif (teamHome.potential == teamAway.potential):
            teamAway.potential -= 1
            return teamAway
        else: return teamHome

    winnerProb = better_team().potential - worse_team().potential + 50 #percentage chance for a win

    def result():
        # print(12 / 5 / 2 * 10)  # score 5
        # print(12 / 5 / 2 * 10)  # score 0
        # print(12 / 4 * 10)  # score 4
        # print(12 / 3 * 10)  # score 1
        # print(12 / 2 * 10)  # score 3
        # print(12 / 1 * 10)  # score 2

        betterTeamScoreProb = []
        adv = better_team().potential - worse_team().potential #advantage
        #totalProb = (adv/5 + adv/4 + adv/3 + adv/2 + adv/1) * 10 #podstawa

        betterTeamScoreFive = (better_team().potential - worse_team().potential)
        for i in range(int(betterTeamScoreFive)):
            betterTeamScoreProb.append(5)


        betterTeamScoreZero = (better_team().potential - worse_team().potential)
        for i in range(int(betterTeamScoreZero)):
            betterTeamScoreProb.append(0)

        betterTeamScoreFour = (better_team().potential - worse_team().potential) // 3.5 * 10
        for i in range(int(betterTeamScoreFour)):
            betterTeamScoreProb.append(4)

        betterTeamScoreOne = (better_team().potential - worse_team().potential) // 3 * 10
        for i in range(betterTeamScoreOne):
            betterTeamScoreProb.append(1)

        betterTeamScoreThree = (better_team().potential - worse_team().potential) // 1.5 * 10
        for i in range(int(betterTeamScoreThree)):
            betterTeamScoreProb.append(3)

        betterTeamScoreTwo = (better_team().potential - worse_team().potential) // 1 * 10
        for i in range(betterTeamScoreTwo):
            betterTeamScoreProb.append(2)


        #worse team
        worseTeamScoreProb = []
        # totalProb = (adv/5 + adv/4 + adv/3 + adv/2 + adv/1) * 10 #podstawa

        worseTeamScoreFive = (better_team().potential - worse_team().potential) // 6
        for i in range(worseTeamScoreFive):
            worseTeamScoreProb.append(5)

        worseTeamScoreFour = (better_team().potential - worse_team().potential) // 5
        for i in range(worseTeamScoreFour):
            worseTeamScoreProb.append(4)

        worseTeamScoreThree = (better_team().potential - worse_team().potential) // 4.5 * 10
        for i in range(int(worseTeamScoreThree)):
            worseTeamScoreProb.append(3)

        worseTeamScoreTwo = (better_team().potential - worse_team().potential) // 3.5 * 10
        for i in range(int(worseTeamScoreTwo)):
            worseTeamScoreProb.append(2)

        worseTeamScoreOne = (better_team().potential - worse_team().potential) // 2 * 10
        for i in range(worseTeamScoreOne):
            worseTeamScoreProb.append(1)

        worseTeamScoreZero = (better_team().potential - worse_team().potential) // 2 // 5 * 10
        for i in range(worseTeamScoreZero):
            worseTeamScoreProb.append(0)

        if(teamHome.name==better_team().name):
            return print("Result is: \n" + better_team().name + " " + str(random.choice(betterTeamScoreProb))+ " - "
                        + str(random.choice(worseTeamScoreProb))+ " " + worse_team().name)
        else:
            return print("Result is: \n" + worse_team().name + " " + str(random.choice(worseTeamScoreProb)) + " - "
                         + str(random.choice(betterTeamScoreProb)) + " " + better_team().name)




    prc_chance_for_win = 'Match between ' + teamHome.name + ' home and ' + teamAway.name + ' away.\n' \
                         + '%s has %d%% chance to win this match' % (better_team().name, winnerProb)
    return print(prc_chance_for_win + "\n"), result()

    # return print(prc_chance_for_win)
    #return(result())



#match(random.choice(teams), random.choice(teams))
#print(match(teams[1], teams[2]))

match(twoTeams()[0], twoTeams()[1])
#bez powtórzeń (jakbym użył random.choices(teams, 2), to mogłyby wystąpić powtórzenia
# team = random.sample(teams, 2)
# match(team[0], team[1])