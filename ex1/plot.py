import numpy as np 
from matplotlib import pyplot as plt 
from gradientdecent import gradientdecent
data = np.loadtxt('ex1data1.txt',delimiter=',')
x = data[:, 0]
y = data[:, 1]
def plot():
	plt.plot(x,y,'rx',10)
	(theta, c, l, n) = gradientdecent(0.01,1500)
	w = np.linspace(5,23,1000)
	z = theta[0] + (w*theta[1])
	plt.plot(w,z,'b-')
	plt.xlabel('Profit in $10,000s')
	plt.ylabel('Population of City in 10,000s')
	return plt.show()
#print plot()
