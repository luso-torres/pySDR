def randomMatrices():
    A = np.random.randn(3,10) #3x10 random
    B = np.arange(10) # 1D array
    B = B.reshape(-1,1) #10x1
    C = A@B #matrix multiply
    print(C.shape)
    C = C.squeeze()
    print(C.shape)