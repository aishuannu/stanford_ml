import numpy as np 
from scipy import linalg
def normalequation(data):
	m = len(data[:, 1])
	z = np.shape(data)
	a = np.ones((m,1))
	b = np.delete(data,-1,1)
	X = np.append(a,b,axis = 1)
	y = data[:, -1].reshape(m,1)
	theta = np.zeros((z[1]-1,1))
	theta = (linalg.inv(X.T.dot(X)).dot(X.T)).dot(y)
  	return theta

#print normalequation(np.loadtxt('ex1data2.txt',delimiter = ','))
