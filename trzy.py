
# def main():
#     print("Witaj świecie!")
# if __name__ == "__main__":
#     main()


# wynik = "3-1"
# wynik = wynik.split("-")
# print(wynik[0]+" "+wynik[1])

import random

aList = [20, 40, 80, 100, 120]
print ("choosing 3 random items from a list using random.sample() function")
sampled_list = random.sample(range(1, 14), 5)
print(sampled_list)