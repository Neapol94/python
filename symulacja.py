import itertools, sqlite3, random, datetime

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


#Funkcja pobiera id @int
#
#Zwraca obiekt @obj
def teamCreate(id):
    cur.execute("SELECT * FROM teams WHERE id = ?", (id,))
    team = cur.fetchall()

    teamObject = Team(team[0]['id'], team[0]['name'], team[0]['potential'], team[0]['stadium'],
                team[0]['symbol'], team[0]['league'], team[0]['points'],
                team[0]['goals_scored'], team[0]['goals_against'], team[0]['form'])
    return teamObject


#Funkcja zwraca tablicę @Array obiektów wszystkich zespołów
def getAllTeams():
    cur.execute("select count(id) from teams")
    teams = []
    for i in range(1, (cur.fetchone()[-1] + 1)):
        teams.append(teamCreate(i))
    return teams

#Przyjmuje tablicę i zwraca wszystkie kombinacje par @Array
def drawTeamsPairs(teams):
    return list(itertools.combinations(teams, 2))




#Losuje datę z przedziału
def dateGen():
    start_date = datetime.date(2010, 1, 1)
    end_date = datetime.date.today()

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    random_date = f"{random_date.day}-{random_date.month}-{random_date.year}"

    return random_date



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



def result(teamHome, teamAway):
    random.choices([0, 1, 2, 3, 4, 5], [2, 7, 39, 32, 14, 6], k=100).pop()
    random.choices([0, 1, 2, 3, 4, 5], [50, 37, 9, 3, 0.7, 0.3], k=100).pop()
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


    for pair in pairs:
        homeTeamObject = pair[0]
        awayTeamObject = pair[1]
        theResult = result(homeTeamObject, awayTeamObject)
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


def simulate_single_random_match():
    teams = getAllTeams()
    random.shuffle(teams)
    team1 = teams[0]
    team2 = teams[-1]

    theResult = result(team1, team2, betterTeamScore(), worseTeamScore())
    if (theResult[1] > theResult[2]):
        return print(f"wynik: {team1.name} {theResult[1]} - {theResult[2]} {team2.name}. Dnia {dateGen()}")
    elif (theResult[1] < theResult[2]):
        return print(f"wynik: {team1.name} {theResult[1]} - {theResult[2]} {team2.name}. Dnia {dateGen()}")
    elif(theResult[1] == theResult[2]):
        return print(f"wynik: {team1.name} {theResult[1]} - {theResult[2]} {team2.name}. Dnia {dateGen()}")

    return "Mecz się nie odbył."


# pairs = drawTeamsPairs(getAllTeamsId())
# print(cupSimulation(pairs))
simulate_single_random_match()

con.commit()
con.close()
