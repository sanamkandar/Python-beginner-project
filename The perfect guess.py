"""
Date : 03 jan 2021
Author: Sanam Kandar
Project: The Perfect guess
"""
import random

print("\t\t\t\t\t\t\t\t\t\t♦THE PERFECT GUESS♦\n")
print("RULES: ♦Player have 10 chances to guess the correct number."
      "\n\t   ♦Score will evaluate through chances taken to guess the number."
      "\n\t   ♦Player have to choose number between 1 to 100 and Enter number only."
      "\n\t   ♦Player who take minimum chances - will Win!.\n")


def rand_num():
    return random.randint(1, 100)


random_num = rand_num()
# print(random_num)
chances = 0

while chances < 10:
    player_num = int(input(f"♦ Guess the number, {10 - chances} chances left: "))
    chances += 1

    if player_num >= 1 and player_num <= 100:

        if player_num < random_num:
            print("You guess small number think large number!\n")
            if chances == 10:
                print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦SCOREBOARD♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n")
                print(f" You can't guess the number, the number was {random_num}.")

        elif player_num > random_num:
            print("You guess large number think small number!\n")
            if chances == 10:
                print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦SCOREBOARD♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n")
                print(f"You can't guess the number, the number was {random_num}.")
        else:
            print("Wow! you guess the correct number.\n")

            print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦SCOREBOARD♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n")
            if chances >= 8:
                print(f"Not bad! you took {chances} chances.")
            elif chances >= 6:
                print(f"Good! you took {chances} chances.")
            elif chances >= 4:
                print(f"Well guess! you took {chances} chances.")
            elif chances >= 2:
                print(f"Amazing! you took {chances} chances.")
            elif chances == 1:
                print(f"Excellent! you took {chances} chances.")
            break
    else:
        print("INVAILD INPUT!")

f = open("high-score.txt")
last_score = f.read()

if int(last_score) > chances:
    print("You just broken the highest score! congrats.")
    with open("high-score.txt", "w") as j:
        high_score = j.write(str(chances))
f.close()