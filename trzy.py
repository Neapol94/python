
# def main():
#     print("Witaj świecie!")
# if __name__ == "__main__":
#     main()


# wynik = "3-1"
# wynik = wynik.split("-")
# print(wynik[0]+" "+wynik[1])

# import random
# #
# # aList = [20, 40, 80, 100, 120]
# # print ("choosing 3 random items from a list using random.sample() function")
# # sampled_list = random.sample(range(1, 14), 5)
# # print(sampled_list)
#
# def teamCompare(firstTeamId, secondTeamId):
#     while(firstTeamId==secondTeamId):
#         secondTeamId = random.choice(range(1, (14)))
#     return print(firstTeamId, secondTeamId)
#
# teamCompare(3,3)

miesiace = []
for i in range(1,13):
    if(i<10): miesiace.append("0"+ str(i))
    else: miesiace.append(str(i))
print(miesiace)