import random as r
import math
from termcolor import cprint
from pyfiglet import figlet_format
from TypesExercises import *
import os
from StringsExercises import *




try:
    while True:
        cprint(figlet_format('Collection'), 'red')
        choice = int(input("What lesson do you want?\n1. Variable Types\n2. String Manipulation"))
        os.system('cls')
        match choice:
            case 1:
                print("Variable Types")
                choice = int(input("What lesson do you want?\n 1. Dice\n2. Leap Years \n3. Dice Game\n4. Division "
                                   "Checker\n5. Dog Age\n6. Points Calc\n"))
                os.system('cls')
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
                os.system('cls')
                print("Strings")
                choice = int(input("What part do you want?\n1. Get Part of word"
                                   "\n2. Showcase different types of print concatenation"
                                   "\n3. Generate Email based on name and join date"
                                   "\n4. Find Year Group based on email"
                                   "\n5. "))
                os.system('cls')
                match choice:
                    case 1:
                        getPartOfWord()
                        input("\nPress enter to continue")
                    case 2:
                        differentTypesOfPrintFormat()
                        input("\nPress enter to continue")
                    case 3:
                        taskUsername()
                        input("\nPress enter to continue")
                    case 4:
                        findYearGroup()
                        input("\nPress enter to continue")

            case 3:
                print("")
                choice = int(input("What lesson do you want?"))
                match choice:
                    case 1:
                        print()

            case 4:
                print("")
                choice = int(input("What lesson do you want?"))
                match choice:
                    case 1:
                        print()


except ValueError as VE:
    print("bro really got a valueerror")