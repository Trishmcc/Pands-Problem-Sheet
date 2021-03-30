# PANDS-PROBLEM-SHEET


# WEEKLY TASKS
## BY: Trish OGrady

## TASK 2

*A program for calculating a persons BMI. The file name is called bmi.py*

### Explanation of code

* These first two lines of code request a user to input their height and weight in kg. I'm using float in my code as the BMI result is in decimal places.

* The next two lines of code convert the height from cm into metres squared using the BMI calculator [1]

* The fifth line of code rounds the BMI to the nearest two decimal places.[2]

* The last line of code prints the result of the calculation.

### References:

1. https://stackoverflow.com/questions/20405610/bmi-calculator-in-python/50386292

2. https://www.w3resource.com/python/built-in-function/round.php


## TASK 3

*This program will input a string and output every second letter in reverse order. The file name is called secondString.py*

### Explanation of code

* The first line of code requests the user to input a string.

* The second line of code outputs a result. For my output I am reversing the string using splicing. 
  I used two semi colons in square brackets to omit one or more characters. 
  I used -2 as it allows every second letter to be chosen in reverse order.[1]

### References:

1. Jaffe, A. (2009). Understanding string reversal via slicing [Online] Available at: https://stackoverflow.com/questions/766141/understanding-string-reversal-via-slicing [Accessed 4 February, 2021].


## TASK 4

*This program will input any positive integer and output the successive values of the following calculation:
Take the current value and if it is even divide by 2 
If the number is odd the multiply by 3 and 1
The program will end if the current value is 1. The file name is called collatz.py*

### Explanation of code

* The first two lines of code request the user to input a number.

* The third line of code is a while loop. I used a Boolean operator. This condition is saying that if x is greater than 1 then its True.[1]

* The next two lines of code implement an if statement. This applies the function so if any number divided by 2 is 0 hence even then divide the number x itself by 2[2]

* The next two lines of code have an else statement applied.  If the number is uneven then multiple by 3 and add 1. I'm using append - Whats before the dot - is added to the array. (x) is what is added to the numbers.

### References:

1. https://www.datacamp.com  
2. https://bit.ly/3w7TxHF

## TASK 5

*A program that outputs whether or not today is a weekday. The file name is called weekday.py*

### Explanation of code

* The first line of code imports the datetime module.[1]

* The second line of code applies the weekday function (returns an integer for the day of the week) and today function (to get the current date) from the datetime - so to get the week number from the date.

* The rest of the code - I'm using a Boolean operator < and > If the week number is less than 5 (element 0-4) then its a week day, and if its greater than 5 then its the weekend.[2]

### References:

1. https://www.w3schools.com/python/python_datetime.asp

2. https://www.xspdf.com/resolution/58438157.html

## TASK 6

*A program that takes a positive floating-point number as input and outputs an approximation of its sqaure root. The file name is called squareRoot.py*

### Explanation of code

* The first line of code uses Issac Newton's square root function.



### References:

Bytes, (2021, February 25) 10 Simple Python Program | Square Root of a Number using Newton's method. https://www.youtube.com/watch?v=FOeSuUkxc5E 

## TASK 7

*A program that reads in a text file and outputs the number of e's it contains. The program should take the filename from an argument on the command line. The file name is called es.py*

### Explanation of code

* The first line of code - sys imports the internal Python module. 

* The sys.argv is taking the input from the command line to open and work with that file and assigning that to i =i
[1] represents the first argument after the python filename. I call the moby dick text from the command line by using python ./es.py moby-dict.txt

* The open function is then applied.  I'm using rt mode to read a text file

* x equals the content of the text file. Count returns the number of times e or E appear in the string.

### References:

https://realpython.com/python-command-line-arguments
https://www.w3schools.com/python/ref_string_count.asp

## TASK 8

*This program displays a plot of functions f(x)=x, g(x)=xsquared and h(x)=x3 
in the range [0, 4] on the one set of axes. The file name is called plottask.py*

### Explanation of code

* Created data in an array for a function f(x)

* Created a function for y and z data points

* The data was plotted by performing a calculation on the y axis - x, xsquared, xcubed

* Labels were created, a legend created and unecessary decimal points removed.

### References:

https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html