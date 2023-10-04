##add


def mainMenu():
    while True:
        choice = input("telefonbok> ")
        seperate = choice.split()
        if 3 != len(seperate):
            print("please follow the format, add name number")
            return
        if seperate[0] == "add":
            addNumber(seperate[1], seperate[2])
        elif seperate[0] == "quit":
            break

def checkIfExists(inputName, inputNumber):
    try: #försöker att lösa av en fil men hanterar fel om den ej finns
        f = open("telefonbok.txt", "r")
    except FileNotFoundError: #skapar filen och gör så att den kan läsas
        f = open("telefonbok.txt", "a")
        f.close
        f = open("telefonbok.txt", "r")
    
    list = f.readlines()
    i= 0
    
    while i < len(list): #går igenom filen och splitrar namned och numret
        nameAndNumber = list[i]
        seperate = nameAndNumber.split(";", 2)
        
        if inputName == seperate[1]: #tittar om namnet redans finns
            print("Name already exists")
            return True #returnerar True för att skicka till addnumber()
        elif inputNumber == seperate[0]: #tittar om numret finns 
            print("Number already exists")
            return True
            
        i += 1
        

def addNumber(inputName, inputNumber):
    if not checkIfExists(inputName, inputNumber): #om namn eller numer inte finns läg till
        keepLog = telefonbok()
        keepLog.name = inputName
        keepLog.number = inputNumber
        
        f = open("telefonbok.txt", "a")
        f.write(keepLog.number + ";" + keepLog.name + ";\n")
        f.close

class telefonbok:
    
    def __init__(self, name=0, number=0):
        self.name = name
        self.number = number


mainMenu()