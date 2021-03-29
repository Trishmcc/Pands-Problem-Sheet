# A program that takes a positive floating-point number as input 
# and outputs an approximation of its sqaure root
# Author: Trish O'Grady


def i(sqrt):

#Input is a positive floating number

    n = float(input('Please enter a positive number:'))

#call a function
# n = 14


approx = 0.5 * 14
better = 0.5 *(approx + 14/approx)

# Output approximation of its square root

print ("The square root of 14 is approx: ", better)


