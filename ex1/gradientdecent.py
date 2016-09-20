import numpy as np 
from computingcost import computingcost
data = np.loadtxt('ex1data1.txt',delimiter=',')
m = len(data[:, 1])
a = np.ones((m,1))
b = data[:, 0].reshape(m,1)
X = np.append(a,b,axis = 1)
y = data[:, 1].reshape(m,1)
def gradientdecent(alpha,num_iter):
	i = 1
	theta = np.zeros((2,1))
	l = np.zeros((num_iter,2))
	n = np.zeros((num_iter,1))
	while i<=num_iter:
		temp0 = 0
		temp1 = 0
		j = 0
		while j < m:
			temp0 = temp0 + (X[j].dot(theta) - y[j])
			temp1 = temp1 + (X[j].dot(theta) - y[j])*data[:, 0][j]
			j += 1
		theta[0] = theta[0] - ((alpha/m)*temp0)
		theta[1] = theta[1] - ((alpha/m)*temp1)
		l[i-1] = theta.T
		c = computingcost(theta)
		n[i-1] = c
		i += 1
	return theta, c, l, n
#print gradientdecent(0.01,1500)  
#theta, c, l, n = gradientdecent(0.01,1500)
#print (np.array([[1,3.5]])).dot(theta)
#print (np.array([[1,7]])).dot(theta)