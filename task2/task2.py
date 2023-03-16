import numpy as np 

M = input('Enter the number of rows:')
N = input ('Enter the number of columns:')

M = int(M)
N = int(N)

b = np.random.randint (0, 2, (M, N))
print ("Matrix:\n", b)

x = np.count_nonzero(b)
print('Number of islands:', x)