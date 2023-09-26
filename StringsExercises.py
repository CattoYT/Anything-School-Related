# 26/9/23
def stringGreaterThan():
    # this works by comparing the ascii value of the first character
    test = "PY" > "Java"
    print(test)


def getPartOfWord():
    string, firstpart, second = input("Give a word"), int(input("Give start letter")), int(input("Give end letter"))
    # takes the characters between firstpart and second, 0 indexed
    output = string[firstpart:second]
    print(output)


def checkSubStrings():
    string, stringToCheck = input("Give a sentence/word "), input("What do I search for? ")
    # yes.
    if stringToCheck in string:
        print(f"{stringToCheck} is in {string}!")


def differentTypesOfPrintFormat():
    lmao = "bob"
    lmao2 = 20
    print("Hello " + lmao)  # adding the strings
    print("Hello ", lmao)  # treat as a list
    print(f"Hello {lmao}")  # embed into string (Based)

    # print only accepts strings so you have to cast it to a string before printing
    print("Hello " + str(lmao2))  # adding the strings
    print("Hello ", lmao2)  # treat as a list
    print(f"Hello {lmao2}")  # embed into string (Based)


def taskUsername():
    yearJoined = input("What year did you join? ")
    surname = input("What is your surname? ")
    firstname = input("What is your first name? ")

    email = f"{yearJoined[2:]}{surname}{firstname[0]}@gmail.com"

    print(email)
def findYearGroup():
    email = input("What is your email? ")
    year = email[0:2]

    match year:
        case '23':
            print("Year 7")
        case '22':
            print("Year 8")
        case '21':
            print("Year 9")
        case "20":
            print("Year 10")
        case "19":
            print("Year 11")
        case "18":
            print("Year 12")

def checkPassword():
    validity = False
    while validity != True:
        password = input("What is your password? ") #lmao
        if len(password) >= 8 and any(i.isdigit() for i in password):
            print("Password is valid")

        else:
            print('NO')
