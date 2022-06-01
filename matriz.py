# librería numpy
import numpy as np

matriz1 = np.array([4,8,7])
print(matriz1, matriz1.shape, type(matriz1), type(matriz1[1]))

matriz2 = np.array([[4,5,7],[3,5,4],[1,9,7]])
print(matriz2, matriz2.shape, type(matriz2), matriz2[2,0])

matriz3 = np.array([
    [[1,2],[3,4],[5,8]],
    [[3,8],[5,7],[2,3]],
    [[3,8],[1,2],[6,40]],
    [[3,8],[1,2],[6,4]]
])
print(matriz3)
print(matriz3.shape)
print(matriz3[2,2,1])