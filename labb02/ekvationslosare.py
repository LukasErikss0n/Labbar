import math

def derivative(f, x, h):
    derivata = (1/(2*h))*((f(x+h)) - (f(x-h)))
    return derivata

def solve(f, x0, h):
    xn = x0 + 1
    while abs(x0 - xn) > h: 
       xn = x0
       x0 = x0 - (f(x0)/derivative(f, x0, h))
       
    return xn
            
def function(x):
  return x**2-1




#import d0009e_lab2_solveTest