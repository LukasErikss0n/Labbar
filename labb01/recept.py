import math 

antal = int(input("Här är ett recept på en sockerkaka, för hur många vill du göra? "))
print("-"*10)



   
def recept(antal):
  ingredienser = {
    "ägg": [3, "st"],
    "strösocker": [3, "dl"],
    "vaniljsocker": [2, "tsk"],
    "bakpulver": [2, "tsk"],
    "vetemjöl": [3, "dl"],
    "smör": [75, "g"],
    "vatten" : [1, "dl"], 
  }
  for keys, values in ingredienser.items():
    antalPerPerson = values[0]/4
    antalPerForFragan = (antalPerPerson*antal)
    roundUpp = math.ceil(antalPerForFragan)
    receptForAntal = keys + ": " + str(roundUpp) + " " + values[1]
    print(receptForAntal) 

def tidblanda(antal):
  blandningstid = 10 + antal
  return blandningstid

def tidsgradda(antal):
  tidMedPersoner = 30 + (antal*3)
  return tidMedPersoner

def sockerkaka(antal):
  tidsatgang = tidsgradda(antal) + tidblanda(antal)
  print("Tidsåtgång: " ,tidsatgang, "min")
  print("-"*10)
  recept(antal)
  
  
def line(linjeLangd):
  print("-"*linjeLangd)
  
sockerkaka(antal)
line(10)
print("Recept för 4 personer: ")
line(10)
sockerkaka(4)
line(10)
print("Recept för 7 personer: ")
line(10)  
sockerkaka(7)





