import numpy as np

a = np.array(([1,1,1],[8,4,7],[4,2,7]))
a = np.matrix(a)
rhs = np.matrix(np.array([15000,78000,46000]))
rhs = np.transpose(rhs)
ia = np.linalg.inv(a)
result = np.dot(ia,rhs)
print(result)