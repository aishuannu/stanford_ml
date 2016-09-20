from gradientdecent import gradientdecent
import numpy as np 
from matplotlib import pyplot as plt
def gplot():
	(theta, c, l, y) = gradientdecent(0.01,1500)
	x = np.linspace(1,1500,1500)
	plt.plot(x,y,'-')
	plt.xlabel("no. of iteration")
	plt.ylabel("j")
	return plt.show()
#print gplot()
