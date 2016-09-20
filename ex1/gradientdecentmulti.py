import numpy as np 
from computingcostmulti import computingcostmulti
def gradientdecentmulti(data,alpha,num_iter):
  m = len(data[:, 1])
  z = np.shape(data)
  a = np.ones((m,1))
  b = np.delete(data,-1,1)
  X = np.append(a,b,axis = 1)
  y = data[:, -1].reshape(m,1)
  i = 1
  theta = np.zeros((z[1],1))
  l = np.zeros((num_iter,z[1]))
  n = np.zeros((num_iter,1))
  while i<=num_iter:
    temp = np.zeros((z[1],1))
    j = 0
    while j < m:
      temp[0] = temp[0] + (X[j].dot(theta) - y[j])
      k = 1
      while k < z[1]:
        temp[k] = temp[k] + (X[j].dot(theta) - y[j])*data[:, k-1][j]
        k += 1
      j += 1
    k1 = 0
    while k1 < z[1]:
      theta[k1] = theta[k1] - ((alpha/m)*temp[k1])
      k1 += 1
    l[i-1] = theta.T
    c = computingcostmulti(data,theta)
    n[i-1] = c
    i += 1
  return theta, c, l, n
print gradientdecentmulti(np.loadtxt('ex1data2.txt',delimiter = ',',dtype = int),0.01,1500)  
#theta, c, l, n = gradientdecent(0.01,1500)
#print (np.array([[1,3.5]])).dot(theta)
#print (np.array([[1,7]])).dot(theta)