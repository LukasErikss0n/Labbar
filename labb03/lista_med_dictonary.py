
def menu_dictonary():
    ordLista = {
    "hej" : "välkomstfras", 
    "xx" : "sss",
    }

    
    while True: #Kör programmet hela tiden tills man vill exita
        
        option = input("1: Lookup\n2: Insert\n3:Exit\n ")
        
        if option == "1":
            searchWorld = input("Vilket ord vill du få förklarat? ")
            
            lookup(searchWorld, ordLista) #Skickar in ordet som man söker tillsamans med listan för ordet och beskrivnings listan
            
        elif option == "2": 
              
            ord = input("Vilket ord vill du lägga till? ")
            insert(ord, ordLista)  #Skickar in ordet som man söker tillsamans med listan för ordet och beskrivnings listan
            
        elif option == "3":
            break #Stopar while loopen
        else:
            print("Put a nummber inbetween the range 1-3")



def lookup(searchWorld, ordLista):
    ordfinns = False
    for keys, value in ordLista.items(): #loopar igenom hela listan
        
        if searchWorld == keys: #finns ordet kommer de att skrivas ut
            ordfinns = True #blir san så att sista if satsen inte stämmer
            print(keys + ": " + value)
    
    if ordfinns == False:
        print("Ordet finns inte i listan")
        

def insert(ord, ordLista):
    if ord not in ordLista:
        explained = input("Skriv en kort beskrivning till ordet " + ord + ": ")
        ordLista.update({ord : explained}) #läger till ord med beskrivning explained i dictonaryn
    else:
        print("ordet finns redan")         

  