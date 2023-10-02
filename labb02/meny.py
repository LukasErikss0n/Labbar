import tvarssumma 
import bounce 
import ekvationslosare

    
def meny(question):
    if question == 1: 
        bouncequestion = int(input("Välj ett naturligt tal för att skapa en bounce effekt: "))
        bounce.bounce(bouncequestion)
    elif question == 2:
        tvarsummaquestion = int(input("Välj ett tal som du vill titta tvärsumman på: "))
        tvarsummaAnswer = tvarssumma.tvarsumman(tvarsummaquestion)
        print( tvarsummaAnswer)
    elif question == 3: 
        ekvationslosarequestion = int(input("Sätt in ett x värde som du vill lösa ekvationen f(x) = x^2 -1: "))
        answer = ekvationslosare.solve(ekvationslosare.function, ekvationslosarequestion, 0.01)
        print(answer)
    else:
        print("Programmet har avslutats ")
    
question = int(input("Välj vad du vill göra \n 1. Bounce \n 2. Tvarsumma \n 3. ekvationslosare \n 4. avsluta program\n"))


meny(question)