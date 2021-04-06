  
# A program that takes a positive floating-point number 14.5 as input 
# and outputs an approximation of its sqaure root 3.8 
# Author: Trish O'Grady

#This is the formaula for Neewtons formula

def squareRoot(n) :
  
#Approximate a value of a function. The error should be small between approx and real value 
#as there is always an error.
    
    x = n 
    m=0.00001 
  
# To count the number of iterations 
      
    while (1) :  
        
# Calculate more closed x 
        
        root = 0.5 * (x + (n / x)) 
  
# Check for closeness # 
        
        if (abs(root - x) < m) :
            break 
  
# Update root 
        
        x = root
  
    return root 
  
if __name__ == "__main__" : 
  
    n = float(input("Enter the number: "))
  
    output=squareRoot(n)
    
    print("The approximate square root is: ",round(output,1))




