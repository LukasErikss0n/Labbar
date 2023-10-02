
def menu_tuple():
    tupleList = [("hej", "välkomen")]
    
    while True: #Kör programmet hela tiden tills man vill exita
        
        option = input("1: Lookup\n2: Insert\n3:Exit\n ")
        
        if option == "1":
            searchWorld = input("Vilket ord vill du få förklarat? ")
            lookup(searchWorld,tupleList ) #Skickar in ordet som man söker tillsamans med listan för ordet och beskrivnings listan
            
        elif option == "2": 
              
            ord = input("Vilket ord vill du lägga till? ")
            insert(ord, tupleList) #Skickar in ordet som man söker tillsamans med listan för ordet och beskrivnings listan
            
        elif option == "3":
            break #Stopar while loopen
        else:
            print("Put a nummber in between the range 1-3")
 

def lookup(searchWorld, tupleList):

    i = 0
    ordFinns = False
    while i < len(tupleList):  #kör en while loop för listans lengd, för att gå igenom varje plats
        if searchWorld == tupleList[i][0]:
            ordFinns = True #säter till True för att sista if satsen inte ska köras 
            print(searchWorld + ": " + tupleList[i][1]) #tar tupleList index +1 eftersom att förklaringen till varje ord är en position backom varje ord
        i = i + 1
    if ordFinns == False:
        print("Ordet finns inte")
        
    return ordFinns
 

def insert(ord, tupleList):
    i = 0 
    while i < len(tupleList): #tittar om ord inte finns i listan
       if ord == tupleList[i][0]:
            return print("ordet finns redan")
       i += 1
    info = input("Skriv en kort beskrivning till ordet " + ord + ": ")
    newWorld = (ord, info) 
    tupleList.append(newWorld) # lägger till ordet + förklaringen till tuplen
    print("Ordet: " + ord + " med berskrivningen: " + info + " har lagt still") 
    

 