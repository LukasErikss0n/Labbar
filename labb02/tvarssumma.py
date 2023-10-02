

def tvarsumman(heltal):
    if heltal:
        heltal = heltal%10 + tvarsumman(heltal//10)
    return heltal
    

def tvarsumman2(heltal):
    sum = 0
    while heltal > 0:
        sum += heltal%10
        heltal = heltal//10
    return sum    
        
    
#import d0009e_lab2_sumTest
    
    
    
#print(tvarsumman2(456))
