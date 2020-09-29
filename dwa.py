import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()


create_connection(r'C:\sqlite\gui\football.db') #musi być r na początku żeby traktowało to w ciapkach jako surowy string





# class Team:
#   def __init__(self, name, potential):
#     self.name = name
#     self.potential = potential

# manutd = Team("ManUtd", 42)
# luton = Team("Luton Town", 21)
#
# def match(team_home, team_away):
#     def better_team(): #which team is better
#         if(team_home.potential>team_away.potential): return team_home
#         else: return team_away
#     def worse_team(): #which team is worse
#         if(team_home.potential>team_away.potential): return team_away
#         else: return team_home
#     prc_chance_for_win = '%s has %d%% chance to win this match' % (better_team().name, better_team().potential - worse_team().potential + 50)
#     return prc_chance_for_win
#
# print(match(manutd, luton))