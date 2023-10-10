class telefonbok:
        def __init__(self):
    
            self.listDic = {}
            kommandonDic = {"add": self.add, 
                            "lookup": self.lookup,
                            "alias": self.alias, 
                            "change": self.change, 
                            "quit" : self.quit, 
                            "save" : self.save, 
                            "load" : self.load, 
                            "show" : self.show,
                            "delete" : self.delete
                            }
            
            while True:
                choice = input("Phonebook> ")
                seperate = choice.split()

                try:
                    kommandonDic[seperate[0]](*seperate[1:])
                except TypeError: #om formatet inte följs ska den skicka felmedelander
                    print("Pleas follow the formant: 'promt' name number")
                except SystemExit:
                    break
                
        def checkIfExists(self, inputName, inputNumber):
            for number, names in self.listDic.items(): #skapar name och number för varje element i dictonarin
                for name in names : 
                    if inputName == name: #tittar om inputname matchar name från listan
                        return True, number, 1
                    elif inputNumber == number: #tittar om inputnumber matchar number från listan
                        return True, 2
                
        def add(self, inputName, inputNumber):
            existOrNot = self.checkIfExists(inputName, inputNumber) #får värdet true med 1 om namnet finns, får värder 2 och true om number redan finns

            if not existOrNot: #tittar om inget finns
                self.listDic[inputNumber] = [inputName]
            elif existOrNot[1] == 2: #om number finns, för specifika felmedelande
                print("number alredy exists")
            elif existOrNot[2] == 1: #om namn finns, för specifika felmedelande
                print("name already exists")
            
            
        def lookup(self, inputName):
            getNumber = self.checkIfExists( inputName, 0) #får ut numret om namnet finns
            if  getNumber:
                print("Phone number for " + inputName + ": " + getNumber[1])
            else:
                print("The name" + inputName + " does not exist")

        def alias(self, inputName, inputAlias):
            getNumber = self.checkIfExists(inputName, 0)
            if getNumber:
                self.listDic[getNumber[1]] += [inputAlias]  #skapar ett alias för inputname 
            else:
                print("The name " + inputName + " does not exist")
    
        def change(self, inputName, inputNewNumber):
            existsOrNot = self.checkIfExists(inputName, inputNewNumber)
            if existsOrNot: #tittar om namnet finns
                if existsOrNot[1] != 2:
                    values = self.listDic[existsOrNot[1]] #sparar infon i dictonaryn för nyckeln inputname
                    del self.listDic[existsOrNot[1]] #tar bort gamla nyckel paret från dictionary
                    self.listDic[inputNewNumber] = values
                else:
                    print("Number already exists")
                
            else:
                print("The name " + inputName + " does not exist" )
        
        def quit(self):
            raise SystemExit #stänger av programmet 
        
        def show(self, promts):
            if promts == "list":
                print("Phone list:")
                for number, names in self.listDic.items(): #visar hela telefonboken
                    for name in names:
                        print(name + ": " + number)
        
        def save(self, saveAs):
            for number, names in self.listDic.items(): #för varje namn pch number i dictonaryn ska det spara det till filen
                for name in names:
                    txtFile = saveAs + ".txt"
                    f = open(txtFile, "a")
                    f.write(number + ";" + name + ";\n")
                    f.close
        
        def load(self, loadFile):
            txtFile = loadFile + ".txt"
            try: #försöker att lösa av en fil men hanterar fel om den ej finns
                f = open(txtFile, "r") #öppnar fillen med namnet loadName
            except FileNotFoundError: #om fill inte finns, skicka felmedelande
                print("the file " + loadFile + " does not exist")
                return
            self.listDic.clear() # filen töms om txt filen finns
            saved = f.readlines() #läser in varje rad från filen
            i= 0
            print("The following names and numbers have been added to the dictonary")
            while i < len(saved): #loopar igenom saved
                nameAndNumber = saved[i]
                seperate = nameAndNumber.split(";", 2) #separar name and number
                self.listDic[seperate[0]] = [seperate[1]]
                print(seperate[1] + ": " + seperate[0])
                i += 1
            f.close
                
        def delete(self, typeOfDelete, deleteFileOrName ):
            if typeOfDelete == "phonebok":
                txtFile = deleteFileOrName + ".txt"
                import os
                if os.path.exists(txtFile):
                    os.remove(txtFile) #raderar filen med namnet txtFile
                else:
                    print("The file does not exist")
            elif typeOfDelete == "name": 
                existsOrNot = self.checkIfExists(deleteFileOrName, 0)
                if existsOrNot:
                    del self.listDic[existsOrNot[1]] #raderar namnet och numret från dictonaryn
                else:
                    print("The " + deleteFileOrName + " do not exist")
            else:
                print("this type of " + typeOfDelete + " delete does not exist")
                
        
            
telefonbok()
        