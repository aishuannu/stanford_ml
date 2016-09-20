import numpy as np 
data = np.loadtxt('ex1data1.txt',delimiter=',')
m = len(data[:, 1])
a = np.ones((m,1))
b = data[:, 0].reshape(m,1)
X = np.append(a,b,axis = 1)
y = data[:, 1].reshape(m,1)
def computingcost(theta):
  c = np.dot(X,theta)
  j = 0
  i = 0
  while i<m:
    j = j + (c[i] - y[i])**2
    i += 1  
  j = j/(2*m)
  return j
#print computingcost(np.zeros((2,1)))
