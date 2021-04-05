# A program that takes a positive floating-point number 14.5 as input 
# and outputs an approximation of its sqaure root 3.8 
# Author: Trish O'Grady

import math as mt

def square_root():
    value=float(input("Enter the number: "))
    sqrt_value=round(mt.sqrt(value),1)
    print("The Approximate square root is: ",sqrt_value)
    
square_root()
#def i(sqrt):

#Input is a positive floating number

    #n = float(input('Please enter a positive number:'))

#call a function
# n = 14.5

#approx = math.sqrt(14.5)
#approx = 0.5 ** 14.5
#better = 0.5 *(approx + 14.5/approx)

# Output approximation of its square root

#print ("The square root of 14.5 is approx: ", better)

#print(approx)




