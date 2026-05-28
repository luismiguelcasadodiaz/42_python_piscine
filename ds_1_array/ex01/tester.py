import numpy as np
from array2D import slice_me


family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]
print(slice_me(family, -2, -2))
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
print(slice_me(family, -1, -2))
family = [[], [], [], []]
print(slice_me(family, 1, -2))

a2D = np.array(family)
print(a2D)
print(a2D[-2:2])
family = [[0, 0],
          [1, 1],
          [2, 2],
          [3, 3],
          [4, 4]]
family = []
a2D = np.array(family)
print("+++[0:0]\n", a2D[0:0])
print("+++[0:1]\n", a2D[0:1])
print("+++[0:2]\n", a2D[0:2])
print("+++[0:3]\n", a2D[0:3])
print("+++[0:4]\n", a2D[0:4])
print("+++[0:5]\n", a2D[0:5])
print("+++[-1:0]\n", a2D[-1:0])
print("+++[-1:1]\n", a2D[-1:1])
print("+++[-1:2]\n", a2D[-1:2])
print("+++[-1:3]\n", a2D[-1:3])
print("+++[-1:4]\n", a2D[-1:4])
print("+++[-1:5]\n", a2D[-1:5])
print("+++[4:5]\n", a2D[4:5])
print("+++[4:-1]\n", a2D[4:-1])
print("+++[4:4]\n", a2D[4:4])
print("+++[2:-4]\n", a2D[2:-4])
print("+++[-4:2]\n", a2D[-4:2])
print("+++[-4:1]\n", a2D[-4:1])
print("+++[-5:1]\n", a2D[-5:1])
print("+++[5:1]\n", a2D[5:1])
print("+++[6:1]\n", a2D[6:1])
