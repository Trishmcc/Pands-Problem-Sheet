# Program for calculating a persons BMI
# Author: Trish OGrady


#Inputting 2 variables named person height and person weight in Kgs
#I'm using float as the BMI result is in decimal places.

height = float(input('What is your height:'))
weight = float(input('What is your weight:'))

#I am converting the height from cm into metres squared

heightmetre = height/100
metreSq = heightmetre**2

# Calculating the BMI. 
# The BMI will be rounded to the nearest 2 decimal places 
# hence round and 2 were used. 
# I found this in w3resource.

BMI = round(weight / metreSq, 2)

# BMI output.
# The + and str were used to make the strings and integers 
# work together.

print ("BMI is " + str(BMI))