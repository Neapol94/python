import sys, random
file = open('plik.txt', 'r')
dane = file.read()

# def main():
#     print("Witaj świecie!")
# if __name__ == "__main__":
#     main()


# wynik = "3-1"
# wynik = wynik.split("-")
# print(wynik[0]+" "+wynik[1])

#
# aList = [20, 40, 80, 100, 120]
# print ("choosing 3 random items from a list using random.sample() function")
# sampled_list = random.sample(range(1, 14), 5)
# print(sampled_list)

# def teamCompare(firstTeamId, secondTeamId):
#     while(firstTeamId==secondTeamId):
#         secondTeamId = random.choice(range(1, (14)))
#     return print(firstTeamId, secondTeamId)
#
# teamCompare(3,3)


# slownik = (
#     {"dzieki":"dziekiinfo","dzieki2":"dziekiinfo2","dzieki3":"dziekiinfo3","dzieki4":"dziekiinfo4"},
#     {"dzieło":"dziełoinfo","dzieło2":"dziełoinfo2","dzieło3":"dziełoinfo3","dzieło4":"dziełoinfo4"},
#     {"jujek":"jujekinfo","jujek2":"jujekinfo2","jujek3":"jujekinfo3","jujek4":"jujekinfo4"},
#     {"ozibambi":"ozibambiinfo","ozibambi2":"ozibambiinfo2","ozibambi3":"ozibambiinfo3","ozibambi4":"ozibambiinfo4"}
# )
#
# for key in slownik:
#     for keyinfo in key:
#         print(keyinfo, "-", key[keyinfo])

# numberGenerator = (element**2
#     for element in range(3)
#     if(element % 2 == 0)
# )
# for item in numberGenerator:
#     print(item)

# names = {"Leszek", "Iza", "Paweł", "Wioletta"}
# celsius = {"c1": -20, "c2": -15, "c3": 0, "c4": 12, "c5": 24, "c6": 21}
# namesLength = {
#     name : len(name)
#     for name in names
# }
# fahrenheit = {
#     key : celsius[key]*1.8+32
#     for key in celsius
#     if celsius[key] > 0
# }
#
# print(fahrenheit)

# liczby = []
# generatorLiczb = (
#     liczba
#     for liczba in range(1, 400)
#     if(liczba % 7 == 0 and liczba % 5 != 0)
# )
#
# for liczba in generatorLiczb:
#     print(liczba)

# rok = str(2016)
# if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
#     print(True)
anagram = "maokai"
#tekst = input("Podaj słowo, sprawdzę czy jest anagramem do %s \n" % anagram)
#tekst = input("Podaj słowo, sprawdzę czy jest palindromem \n")

def czyAnagram(tekst, anagram):
    n = len(tekst)
    if len(anagram) != n:
        return False

    slownik1 = dict()
    slownik2 = dict()
    for i in range(n):
        if tekst[i] in slownik1:
            slownik1[tekst[i]] += 1
        else:
            slownik1[tekst[i]] = 1
        if tekst[i] in slownik2:
            slownik2[tekst[i]] += 1
        else:
            slownik2[tekst[i]] = 1
    return slownik1==slownik2


def czyPalindrom(tekst):
    n = len(tekst)
    if(n != len(tekst)):
        return False
    bufor = ""
    for i in range(n):
        bufor += (tekst[-1*(i+1)])
    return bufor==tekst

def najwiekszaZListy(lista):
    najw = [0, 0]
    n = len(lista)
    for i in range(n):
        if(lista[i]>najw[0]):
            najw[1] = najw[0]
            najw[0] = lista[i]
    return najw

lista = [2, 3, 4, 5, 6, 7, 2, 2, 2]

#print(najwiekszaZListy(lista))



def sprawdzVM(list):
    n = len(list)
    listaVM = []
    powtorki = []
    for i in range(n):
        if(i<n-10):
            if(list[i]+list[i+1]=="VM"):
                listaVM.append(list[i:i+6])
        else:
            break
    for vm in range(len(listaVM)):
        currentVM = listaVM[vm]
        for i in range(len(listaVM)):
            if(currentVM in powtorki):
                break
            elif (currentVM == listaVM[i] and vm != i):
                powtorki.append(currentVM)
    return powtorki




print(sprawdzVM(dane))
#print(czyPalindrom(tekst))
#print(czyAnagram(tekst, anagram))