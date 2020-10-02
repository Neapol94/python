# import sqlite3
# from sqlite3 import Error


#
# try:
#     connection = sqlite3.connect('football.db')
#     cursor = connection.cursor()
# except Error as e:
#     print(e)


# try:
#     connection = sqlite3.connect('football.db')
#     cursor = connection.cursor()
#
#     cursor.execute("SELECT * FROM teams")
#     rows = cursor.fetchall()
#
#     for row in cursor.fetchall():
#         print(row)
# except sqlite3.Error as error:
#     print(error)
# finally:
#     if(connection):
#         connection.close()
#         print("connection closed")



# cursor.execute("create table if not exists teams("
#                "id integer PRIMARY KEY,"
#                "name text NOT NULL,"
#                "symbol text NOT NULL,"
#                "stadium text NOT NULL,"
#                "league_level text NOT NULL"
#                ");")


import random
class Team:
  def __init__(self, name, potential):
    self.name = name
    self.potential = potential

teams = []
teams.append(Team("ManUtd", 42))
teams.append(Team("Luton Town", 21))
teams.append(Team("Chelsea", 44))
teams.append(Team("Brentford", 26))
teams.append(Team("Brighton", 29))
teams.append(Team("Everton", 34))
teams.append(Team("Birmingham", 27))
teams.append(Team("Newcastle", 33))
teams.append(Team("West Ham", 30))
teams.append(Team("Liverpool", 48))
teams.append(Team("Bournemouth", 32))
teams.append(Team("Watford", 28))
teams.append(Team("Norwich City", 28))
teams.append(Team("ManCity", 45))
teams.append(Team("Blackburn Rovers", 25))
teams.append(Team("Sheffield United", 34))
teams.append(Team("Wolves", 39))
teams.append(Team("Arsenal", 40))
teams.append(Team("Tottenham", 41))
teams.append(Team("Leicester", 40))

def match(teamHome, teamAway):
    def better_team(): #which team is better
        teamHome.potential += 2
        if(teamHome.potential>teamAway.potential): return teamHome
        elif(teamHome.potential == teamAway.potential):
            teamHome.potential +=1
            return teamHome
        else: return teamAway
    def worse_team(): #which team is worse
        teamAway.potential -= 3
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

        betterTeamScoreFour = (better_team().potential - worse_team().potential) / 4 * 10
        for i in range(int(betterTeamScoreFour)):
            betterTeamScoreProb.append(4)

        betterTeamScoreOne = (better_team().potential - worse_team().potential) / 3 * 10
        for i in range(int(betterTeamScoreOne)):
            betterTeamScoreProb.append(1)

        betterTeamScoreThree = (better_team().potential - worse_team().potential) / 2 * 10
        for i in range(int(betterTeamScoreThree)):
            betterTeamScoreProb.append(3)

        betterTeamScoreTwo = (better_team().potential - worse_team().potential) / 1 * 10
        for i in range(int(betterTeamScoreTwo)):
            betterTeamScoreProb.append(2)


        #worse team
        worseTeamScoreProb = []
        # totalProb = (adv/5 + adv/4 + adv/3 + adv/2 + adv/1) * 10 #podstawa

        worseTeamScoreFive = (better_team().potential - worse_team().potential)/ 5
        for i in range(int(worseTeamScoreFive)):
            worseTeamScoreProb.append(5)

        worseTeamScoreFour = (better_team().potential - worse_team().potential)/ 4
        for i in range(int(worseTeamScoreFour)):
            worseTeamScoreProb.append(4)

        worseTeamScoreThree = (better_team().potential - worse_team().potential) / 4 * 10
        for i in range(int(worseTeamScoreThree)):
            worseTeamScoreProb.append(3)

        worseTeamScoreTwo = (better_team().potential - worse_team().potential) / 3 * 10
        for i in range(int(worseTeamScoreTwo)):
            worseTeamScoreProb.append(2)

        worseTeamScoreOne = (better_team().potential - worse_team().potential) / 2 * 10
        for i in range(int(worseTeamScoreOne)):
            worseTeamScoreProb.append(1)

        worseTeamScoreZero = (better_team().potential - worse_team().potential) / 1 * 10
        for i in range(int(worseTeamScoreZero)):
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
match(random.choice(teams), random.choice(teams))