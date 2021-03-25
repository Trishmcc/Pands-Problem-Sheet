# A program that takes a positive floating-point number as input 
# and outputs an approximation of its sqaure root
# Author: Trish O'Grady


def i(sqrt):

#Input is a positive floating number

    n = float(input('Please enter a positive number:'))

#call a function
# n = 14.5


approx = 0.5 * 14.5
better = 0.5 *(approx + 14.5/approx)

# Output approximation of its square root

print ("The square root of 14.5 is approx: ", better)


