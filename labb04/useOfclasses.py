class telefonbok:
        def __init__(self):
    
            self.listDic = {}
            kommandonDic = {"add": self.addNameAndNumber, "lookup": self.lookup,
                        "alias": self.alias, "change": self.change, "quit" : self.quit, "save" : self.save, "load" : self.load}
            #self.listDic[name] = number
            
            while True:
                choice = input("telefonbok> ")
                seperate = choice.split()

                try:
                    kommandonDic[seperate[0]](*seperate[1:])
                except TypeError: #om formatet inte följs ska den skicka felmedelander
                    print("Pleas follow the formant: 'promt' name number")
                except SystemExit:
                    break
                
        def checkIfExists(self, inputName, inputNumber):
            for name, number in self.listDic.items(): #skapar name och number för varje element i dictonarin
                if inputName == name: #tittar om inputname matchar name från listan
                    return True, number, 1
                elif inputNumber == number: #tittar om inputnumber matchar number från listan
                    return True, 2
                
        def addNameAndNumber(self, inputName, inputNumber):
            existOrNot = self.checkIfExists( inputName, inputNumber) #får värdet true med 1 om namnet finns, får värder 2 och true om number redan finns

            if not existOrNot: #tittar om inget finns
                self.listDic[inputName] = inputNumber
            elif existOrNot[1] == 2: #om number finns, för specifika felmedelande
                print("number alredy exists")
            elif existOrNot[2] == 1: #om namn finns, för specifika felmedelande
                print("name already exists")
            
            
        def lookup(self, inputName):
            getNumber = self.checkIfExists( inputName, 0) #får ut numret om namnet finns
            if  getNumber:
                print("Telefonnumret för " + inputName + ": " + getNumber[1]) 
            else:
                print("The name" + inputName + " does not exist")

        def alias(self, inputName, inputAlias):
            getNumber = self.checkIfExists(inputName, 0)
            if getNumber:
                self.listDic[inputAlias] = getNumber[1] #skapar ett alias för inputname 
            else:
                print("The name " + inputName + "does not exist")

        def change(self, inputName, inputNewNumber):
            existsOrNot = self.checkIfExists(inputName, inputNewNumber)
            if existsOrNot: #tittar om namnet finns
                if existsOrNot[1] != 2:
                    self.listDic.update({inputName: inputNewNumber}) #bytter numret för inputname
                else:
                    print("Number already exists")
                
            else:
                print("The name " + inputName + " does not exist" )
        
        def quit(self):
            raise SystemExit #stänger av programmet 
        
        def save(self, saveAs):
            for name, number in self.listDic.items(): 
                txtFile = saveAs + ".txt"
                f = open(txtFile, "a")
                f.write(number + ";" + name + ";\n")
                f.close
        
        def load(self, loadFile):
            try: #försöker att lösa av en fil men hanterar fel om den ej finns
                txtFile = loadFile + ".txt"
                f = open(txtFile, "r")
                saved = f.readlines()
                i= 0
                print("The following names and numbers have been added to the dictonary")
                while i < len(saved):
                    nameAndNumber = saved[i]
                    seperate = nameAndNumber.split(";", 2)
                    self.listDic[seperate[1]] = seperate[0]
                    print(seperate[1] + ": " + seperate[0])
                    i += 1
            except FileNotFoundError:
                print("the file " + loadFile + " does not exist")
            self.listDic.clear()
            
            
        
            

        
            
        
            
            
                
            
            
            
            

            
                

telefonbok()
        