import random as r
import time

def daysOfTheWeek():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(days[1]) #prints tuesday

def simonSays():
    instructions = ["Type \"Chicken\"!", "Type \"BokBok\"!",
              "Type \"AUFAUFAF\"!", "Press \"Ctrl + C\"! ;)",
              "Hands on shoulders"]
    score = 0
    while True:

        if r.randint(1, 100)%2 == 0:
            index = r.randint(0, 4)
            check = input("Simon says " + instructions[index])

            match index:
                case 0:
                    if check != "Chicken":
                        print("LMAO L BOZO")
                        score = score-1
                        continue
                case 1:
                    if check != "BokBok":
                        print("LMAO L BOZO")
                        score = score - 1
                        continue
                case 2:
                    if check != "AUFAUFAF":
                        print("LMAO L BOZO")
                        score = score - 1
                        continue
                case 3:
                    if check != "Ctrl + C":
                        print("LMAO L BOZO")
                        score = score - 1
                        continue
            score = score+1


        else:
            deez = input(instructions[r.randint(0, 4)])

            if deez != "":
                print("LMAO L BOZO I DIDNT SAY SIMON SAYS")
                exit(0)

        time.sleep(2)
        print("Score: " + str(score) + "\n\n")

def shoppingList():
    shoppingList = []
    while True:
        item = input("Do you want to add or remove an item?")
        if item == "1":
            add = input("What do you want to add? ")
            shoppingList.append(add)
        elif item == "2":
            remove = input("What do you want to remove? ")

            shoppingList.pop(shoppingList.index(remove))
        elif item == "3":
            break

    print(shoppingList)

