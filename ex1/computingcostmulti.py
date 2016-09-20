import numpy as np 
def computingcostmulti(data,theta):
	m = len(data[:, 1])
	z = np.shape(data)
  	a = np.ones((m,1))
  	b = np.delete(data,-1,1)
  	X = np.append(a,b,axis = 1)
  	y = data[:, -1].reshape(m,1)
  	difference = X.dot(theta) - y
  	vector = difference.T.dot(difference)
  	j = (1.0/(2*m))*vector
  	return j

#print computingcostmulti(np.loadtxt('ex1data2.txt',delimiter = ','),np.zeros((3,1)))
