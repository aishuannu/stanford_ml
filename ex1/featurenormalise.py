import numpy as np
data = np.loadtxt('ex1data2.txt',delimiter = ',')
def featurenormalise(x):
  m = len(x)
  mu = np.mean(x)
  sigma = np.std(x)
  i = 0
  while i < m:
    x[i] = (x[i] - mu)/sigma
    i += 1
  return x
#print featurenormalise(data[:, 1]) 