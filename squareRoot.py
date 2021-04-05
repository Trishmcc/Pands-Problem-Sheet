# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 14:38:23 2021

@author: IVth Hokage
"""
  
# Function to return the square root of 
# a number using Newtons method 
def squareRoot(n) :
  
    # Assuming the sqrt of n as n only 
    x = n 
    m=0.00001
  
    # To count the number of iterations 
    count = 0 
  
    while (1) :
        count += 1 
  
        # Calculate more closed x 
        root = 0.5 * (x + (n / x)) 
  
        # Check for closeness 
        if (abs(root - x) < m) :
            break 
  
        # Update root 
        x = root
  
    return root 
  
if __name__ == "__main__" : 
  
    n = float(input("Enter the number: "))
  
    output=squareRoot(n)
    
    print("The approximate square root is: ",round(output,1))




