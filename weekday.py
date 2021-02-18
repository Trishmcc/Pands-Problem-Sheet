# Program that outputs whether or not today is a weekday
# Author: Trish O'Grady

import datetime

# I'm using the weekday function (returns an integer for the day of the week) and today function
# (to get the current date) from the datetime.
# so to get the week number from the date
weekNumber = datetime.datetime.today().weekday()

# I'm using a Boolean operator < and > If the week number is less than 5 (element 0-4) then its a week day. 
# and if its greater than 5 then its the weekend
if weekNumber > 5:
    print("Yes, unfortunately, today is a week day")
else:
    print ("It is the weekend, Yay!")




