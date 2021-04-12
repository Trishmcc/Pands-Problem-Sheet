  
# A program that takes a positive floating-point number 14.5 as input 
# and outputs an approximation of its sqaure root 3.8 
# Author: Trish O'Grady

#The following function is used to approximate square root for a real number
#using Newton's approximation method.
    
def squareRoot(n) :
  
#Approximate a value of a function. The error should be small between approx and real value 
#as there is always an error.

#N be any number then the square root of N can be given by the formula:
    #1. root = 0.5 * (Guess + (N / Guess)) where X is any guess which can be assumed to be N.
    #2. In the above formula, Guess is any assumed square root of N and root is the correct square root of N.
    #3. Tolerance limit i.e., tolerance in the below code, is the maximum difference between Guess and root allowed.
    
    #Assuming the sqrt of n as n only
    
    Guess = n 
    tolerance=0.00001 
  
# To count the number of iterations 
# Looping until the difference between the approximated root and allowed root is less that the toleranc limit.
      
    while (1) :  
        
# Calculate more closed x 
        
        root = 0.5 * (Guess + (n / Guess)) 
  
# Check for closeness of approximation to allowed square root.
        
        if (abs(root - Guess) < tolerance) :
            break 
  
# Update guess to the  new approximation
        
        Guess = root
  
    return root 
  
if __name__ == "__main__" : 
  
    n = float(input("Enter the number: "))
  
    output=squareRoot(n)
    
    print("The approximate square root is: ",round(output,1))




