# A program that reads in a text file and outputs the number of e's it contains
# Author: Trish O'Grady

#moby-dict.txt
# 116960

# sys imports the internal Python module 

import sys

i = sys.argv[+1]
 # First I will open a file using the open function I'm using rt mode to read a text file


with open(i, "rt") as f:

#x equals the content of the text file
    x = f.read()
    y=x.count("e") + x.count("E")
print(y)
    #while x == f.read(1):
     #   if x == "e" or x == "E":
      #      z = 1

# y is everything that isn't an e and the +1 will add every e found in the text
       # else:
           
        #    z = 0
        #y = y + z
    #print(y)





            # argv.py


#print(f"Name of the script      : {sys.argv[0]=}")
#print(f"Arguments of the script : {sys.argv[+1]=}")

#print (x)
