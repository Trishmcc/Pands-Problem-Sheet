# This program will input any positive integer and output the successive values of the following calculation:
# Take the current value and if it is even divide by 2 
# If the number is odd the multiply by 3 and 1
# The program will end if the current value is 1
# Author: Trish O'Grady


# Want the answer as a whole number so using int for the input
# numbers generated will be placed in an array

x = int(input("Please enter a number: "))
numbers = [x]

# I'm using the Boolean operator  - While - 
# This condition is saying that 
# if x is greater than 1 then its True

while x > 1:

# The indentation repeats this Boolean operation until 
# all calculaions are completed
# The if statement applies the function so 
# if any number divided by 2 is 0 hence even 
# then divide the number x itself by 2
    
    if (x % 2) == 0:
         x = int(x / 2)
     
     # if the number is uneven
     # then multiple by 3 and add 1 
     # I'm using append - Whats before the dot - is added to the array.
     # (x) is what you are adding to the numbers  
    
    else: 
        x = int(x * 3 + 1)

    numbers.append (x)

       

print(numbers)

