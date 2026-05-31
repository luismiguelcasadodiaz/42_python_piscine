import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

datos = [[[120, 111, 132],
          [139, 130, 151],
          [155, 146, 167],
          [0, 255,   0],
          [131, 136,  82],
          [138, 143,  89]],
         [[0,   0,  255],
          [98, 113,  84],
          [112, 127,  96],
          [120, 156,  94],
          [119, 154,  90],
          [255, 0,  0]]]
arr = np.array(datos, dtype=np.uint8)
print(arr.shape)
print(arr)
im = Image.fromarray(arr).convert("L")
plt.imshow(im, cmap='gray')
plt.show()
gray_arr = np.array(im, dtype=np.uint8)
gray_arr = gray_arr[:, :, np.newaxis]
print(gray_arr.shape)
print(gray_arr)
