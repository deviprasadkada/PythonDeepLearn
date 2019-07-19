import numpy as numpy
import matplotlib.pyplot as plot
from sklearn import linear_model

# Creating Numpy Arrays for x and y
#x = numpy.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

x = numpy.array([2.9,6.7,4.9,7.9,9.8,6.9,6.1,6.2,6,5.1,4.7,4.4,5.8])

y = numpy.array([4,7.4,5,7.2,7.9,6.1,6,5.8,5.2,4.2,4,4.4,5.2])

# Loading Linear Model
linear_mod = linear_model.LinearRegression

# Calculating Mean
meanOfX = numpy.mean(x)
meanOfY = numpy.mean(y)
print(meanOfX)
# Calculating the Slope
slope = numpy.sum((x-meanOfX) * (y-meanOfY)) / numpy.sum(numpy.power(x-meanOfX, 2))

# Calculating the Intercept
intercept = meanOfY-(slope * meanOfX)

# Data [mX+b]
data = (slope * x) + intercept
print(data)

plot.plot(x, y)
plot.plot(x, data)
plot.show()