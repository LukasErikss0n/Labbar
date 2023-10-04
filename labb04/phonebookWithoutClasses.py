


def mainMenu():
    listDic = {}
    
    while True:
        choice = input("telefonbok> ")
        seperate = choice.split()

        try:
            if seperate[0] == "add":
                addNameAndNumber(listDic,seperate[1], seperate[2])
            elif seperate[0] == "lookup":
                lookup(listDic, seperate[1])
            elif seperate[0] == "alias":
                alias(listDic, seperate[1], seperate[2])
            elif seperate[0] == "change":
                change(listDic, seperate[1], seperate[2])
        except IndexError: #om formatet inte följs ska den skicka felmedelander
            print("Pleas follow the formant: 'promt' name number")
             
        if seperate[0] == "quit":
            break

def checkIfExists(listDic, inputName, inputNumber):
    for name, number in listDic.items(): #skapar name och number för varje element i dictonarin
        if inputName == name: #tittar om inputname matchar name från listan
            return True, number, 1
        elif inputNumber == number: #tittar om inputnumber matchar number från listan
            return True, 2
        
def addNameAndNumber(listDic, inputName, inputNumber):
    existOrNot = checkIfExists(listDic, inputName, inputNumber) #får värdet true med 1 om namnet finns, får värder 2 och true om number redan finns

    if not existOrNot: #tittar om inget finns
        listDic[inputName] = inputNumber
    elif existOrNot[1] == 2: #om number finns, för specifika felmedelande
        print("number alredy exists")
    elif existOrNot[2] == 1: #om namn finns, för specifika felmedelande
        print("name already exists")
    
      
def lookup(listDic, inputName):
    getNumber = checkIfExists(listDic, inputName, 0) #får ut numret om namnet finns
    if  getNumber:
        print("Telefonnumret för " + inputName + ": " + getNumber[1]) 
    else:
        print("The name" + inputName + " does not exist")

def alias(listDic, inputName, inputAlias):
    getNumber = checkIfExists(listDic, inputName, 0)
    if getNumber:
        listDic[inputAlias] = getNumber[1] #skapar ett alias för inputname 
    else:
        print("The name " + inputName + "does not exist")

def change(listDic, inputName, inputNewNumber):
    existsOrNot = checkIfExists(listDic, inputName, inputNewNumber)

    if existsOrNot: #tittar om namnet finns
        if existsOrNot[1] != 2:
            listDic.update({inputName: inputNewNumber}) #bytter numret för inputname
        else:
            print("Number already exists")
        
    else:
        print("The name " + inputName + " does not exist" )
        


mainMenu()
