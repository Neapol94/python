# napis = "dopa"
#
# if napis == "dopa":
#     print("To jest: %s" % napis)

litery = ["A", "B", "C", "D", "E", "F", "G", "H"]
cyfry = ["1", "2", "3", "4", "5", "6", "7", "8"]
pola = []
i=0
j=0

for i in range(len(litery)):

    for j in range(len(cyfry)):
        pola.append(litery[i]+cyfry[j])


     #print(cyfry[i-1])

print(pola)