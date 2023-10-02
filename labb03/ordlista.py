import lista_med_2_strangar  
import lista_med_tuple
import lista_med_dictonary


print("Här är en ett program för en ordlista, nedan kan du se vad du kan göra")

         
def main_menu():
    choice = int(input("1: Two list\n2: Tuple\n3: Dictonary\n which type do you want to use? "))   
    if choice == 1:
        lista_med_2_strangar.menu_twoLists() 
    elif choice ==2:
        lista_med_tuple.menu_tuple() 
    else:
        lista_med_dictonary.menu_dictonary()   
  

main_menu()
