import random as r
import math


#25/9/23
def diceCalc():
    diceSizes = int(input("give sides"))

    output = r.randint(1, diceSizes)

    print(output)
    return output


def leapYear():
    year = int(input("give year"))

    if (year % 4 == 0):
        print("Leap year!")
        return True
    else:
        print("no idiot")
        return False


def scoreDice(dice1, dice2, dice3):
    if (dice1 == dice2 and dice1 == dice3):
        score = dice1 + dice2 + dice3

    else:
        if (dice1 == dice2):
            score = dice1 + dice2
            score = score - dice3

        elif (dice1 == dice3):
            score = dice1 + dice3
            score = score - dice2

        elif (dice2 == dice3):
            score = dice2 + dice3
            score = score - dice1

        else:
            score = 0

    print(score)


def divisionChecker():
    number1 = int(input("give first number"))
    number2 = int(input("number 2 pls"))

    if number2 == 0 or (number1 % number2 == 1):
        print('False')
    else:
        print('True')


def dogAgeCalc():
    dogAge = float(input("Dogage "))

    if dogAge > 2:
        trueDogAge = 24 + 6 * (dogAge - 2)

    if dogAge <= 2:
        trueDogAge = dogAge * 12
    return trueDogAge


def calculatePoints():
    timespent = int(input("How long did it take lmao "))
    totalcost = 1.00
    if timespent < 15:
        timespent = 15
        print(timespent)
    totalcost = 1.00 + (timespent * 0.20)

    points = timespent * 1.5
    points = math.floor(points)

    print(f"The total cost was £{totalcost}0 and you gained {points} points.")