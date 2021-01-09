"""
Date: 8 jan 2021
Author: sanam kandar
Project: Dice rolling
"""
import random

print("\t\t\t\tDICE ROLLING SIMULATOR\n")
reponse = True
times = True
while reponse:
    if times:
        user = input("Hello do you want to roll this dice? (y/n): ").lower()
        times = False
    else:     
        user = input("do you want to roll again? (y/n): ").lower()
    
    if user == "y":
        dice = random.randint(1,6)
        if dice == 1:
            print("     ")
            print("  ♦  ")
            print("     ")
        elif dice == 2:
            print("    ♦")
            print("     ")
            print("♦    ")
        elif dice == 3:
            print("    ♦")
            print("  ♦  ")
            print("♦    ")
        elif dice == 4:
            print("♦   ♦")
            print("     ")
            print("♦   ♦")
        elif dice == 5:
            print("♦   ♦")
            print("  ♦  ")
            print("♦   ♦")
        elif dice == 6:
            print("♦ ♦ ♦")
            print("♦ ♦ ♦")
            print("♦ ♦ ♦")
    else:
        reponse = False
        print("THANK YOU !!!!!!!!!!!")