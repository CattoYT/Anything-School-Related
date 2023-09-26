import random as r
import math
from termcolor import cprint
from pyfiglet import figlet_format
from TypesExercises import *
from StringsExercises import *

cprint(figlet_format('Collection'), 'Orange')


try:
    while True:
        choice = int(input("What lesson do you want?"))

        match choice:
            case 1:
                print("Variable Types")
                choice = int(input("What lesson do you want?"))
                match choice:
                    case 1:
                        diceCalc()
                    case 2:
                        leapYear()
                    case 3:
                        scoreDice(int(input("put in a number")), int(input("put in a number")), int(input("put in a number")))
                    case 4:
                        divisionChecker()
                    case 5:
                        print(dogAgeCalc())
                    case 6:
                        calculatePoints()
            case 2:
                print("Strings")
                choice = int(input("What lesson do you want?"))
except ValueError as VE:
    print("bro really got a valueerror")