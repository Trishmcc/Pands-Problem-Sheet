# This program displays a plot of functions f(x)=x, g(x)=xsquared and h(x)=x3 
# in the range [0, 4] on the one set of axes

import numpy as np

import matplotlib.pyplot as plt

#xpoints = np.array(range[0, 4])
xpoints = np.array([0, 4])
ypoints = np.array([0, 4])
#f(x)=x
#w = x

# the function -  which is x = x^2 

#y = x*2
#ypoints = (0, 1, 4, 9,)

# the function -  which is x = x^3 
#z = x**3

plt.plot(xpoints, ypoints)
#, label="w")
plt.show()

#plt.plot(xpoints, y)
#plt.show()


#plt.plot(xpoints, label="w")
#plt.plot(xpoints, label="xsquared")
#plt.plot(xpoints, label="x3")