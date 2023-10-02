
def menu_twoLists():
    ordlista = ["hej"]
    forklaringTillOrd = ["välkomen"]

    
    while True: #Kör programmet hela tiden tills man vill exita
        
        option = input("1: Lookup\n2: Insert\n3:Exit\n ")
        
        if option == "1":
            searchWorld = input("Vilket ord vill du få förklarat? ")
            
            lookup(searchWorld, ordlista, forklaringTillOrd) #Skickar in ordet som man söker tillsamans med listan för ordet och beskrivnings listan
            
        elif option == "2": 
              
            ord = input("Vilket ord vill du lägga till? ")
            insert(ord, ordlista, forklaringTillOrd)  #Skickar in ordet som man söker tillsamans med listan för ordet och beskrivnings listan
            
        elif option == "3":
            break #Stopar while loopen
        else:
            print("Put a nummber inbetween the range 1-3")


def lookup(searchWorld, ordlista, forklaringTillOrd ):
    
    i = 0
    ordFinns = False
    while i < len(ordlista): #kör en while loop för listans lengd, för att gå igenom varje plats
        if searchWorld == ordlista[i]: 
            ordFinns = True #säter till True för att sista if satsen inte ska köras 
            print(searchWorld + ": " + forklaringTillOrd[i])
            break
        i = i + 1
    if ordFinns == False:
        print("Ordet finns inte")
        

#Läger till ord om det inte finns, om de redan finns skickas de ut ett felmedelande och ordet lägs inte till 
def insert(ord, ordlista, forklaringTillOrd):
    
    if  ord not in ordlista: #tittar om ord inte finns i listan 
        info = input("Skriv en kort beskrivning till ordet " + ord + ": ")
        ordlista.append(ord)
        forklaringTillOrd.append(info)
        
        print("Ordet: " + ord + "med berskrivningen:" + info + " har lagt still") 
    else:
        print("Ordet finns redan")


