import numpy as np
#def randomMatrices():
A = np.random.randn(3,5) #3x10 random
print('Matrix A:\n',A)
B = np.arange(5)
b = B# 1D array
print('Matrix B:\n',B)
B =np.concatenate([B,b])
print('New Matrix B\n:',B)
B =np.concatenate([B,b])
B = B.reshape(3,5) #10x1
print('Newest Matrix B:\n',B)
B = B.T
print('Newest Matrix B:\n',B)

#
# C = A@B
#print('A*B elementwise:\n',C)
# print(f"transpose of Matrix: {B}")
# C = A@B #matrix multiply
# print("Matrix C",C)
# print(f'Matrix Shape {C.shape}')
# C = C.squeeze()
# print(f'I dont know what is this{C}')
# print(f'Matrix Shape 2 {C.shape}')