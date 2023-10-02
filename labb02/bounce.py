
#n = int(input("välj ett naturligt tal: "))


def bounce(n):
    if(n >= 0):
        print(n)
        bounce(n-1)
        
        if n:
            print(n)
   
   
def bounce2(n):
    i=n
    while n >= 0:
        print(n)
        n -= 1
        if n == 0:
            while n <= i:
                print(n)
                n += 1
            break
      

   
    
#import d0009e_lab2_bounceTest       
          
    
    
    
        
        
#bounce(n)
#bounce2(n)