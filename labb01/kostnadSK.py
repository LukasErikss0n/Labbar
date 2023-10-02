print("Lägg till totala lånet, räntan och antal år för att beräkna totala lånet")

p = int(input("Totala lånet: "))
r = float(input("Räntan: "))
a = int(input("Antal år: "))

#Beräknar totala kostnaden av ett lån enligt s k modelen
def kostnad(p, r, a):
    print("totala kostnaden = ", p+((a + 1)*p*r/2))
    
    

kostnad(p, r, a)

