# This program displays a plot of functions f(x)=x, g(x)=xsquared and h(x)=x3 
# in the range [0, 4] on the one set of axes
# Author: Trish O'Grady

import numpy as np

import matplotlib.pyplot as plt

#create data in an array for a function f(x)

xpoints = np.array(range(0, 4))
ypoints = np.array(range(0, 4))

#create a function for y and z data points

y = xpoints ** 2
z = xpoints ** 3

#Plot the data

plt.plot(xpoints, ypoints, label = "x")
plt.plot(y, label = "xsquared")
plt.plot(z, label = "xcubed")

#Create labels

plt.title('My First MatPlotlib Graph', fontdict={'fontname': 'Aerial', 'fontsize': 12})
plt.xlabel('x Axis')
plt.ylabel('y Axis')

#Describe the contents of the map

plt.legend()

#Deleting unecessary decimal places

plt.xticks([0, 1,2,3])

#plt.show()

plt.savefig("plot.png")


