import numpy as np

# Matrix M:
x = np.arange(9)
M = x.reshape(3, 3)

# vector v:
v = np.array([[1, 2, 3]]).reshape(3,1)

# print them:
print(f'M = \n {M}')
print(f'v = \n {v}')

# print the product:
M_dot_v = np.dot(M, v)
print(f'<M, v> = \n {M_dot_v}')

"This string should appear in remote repo"
