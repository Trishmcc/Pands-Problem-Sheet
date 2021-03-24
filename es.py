# A program that reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line.
# Author: Trish O'Grady


# sys imports the internal Python module 

import sys

# sys.argv is taking the input from the command line to open and work with that file
# and assigning that to = i
# [1] represents the first argument after the python filename.
# I call the moby dick text from the command line by using python ./es.py moby-dict.txt

i = sys.argv[+1]

# First I will open a file using the open function I'm using rt mode to read a text file

with open(i, "rt") as f:

# x equals the content of the text file
# w3schools - count returns the number of times e or E appear in the string.

    x = f.read()
    y=x.count("e") + x.count("E")
print(y)