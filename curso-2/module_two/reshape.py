import numpy as np

array_1d = np.arange(10)
array_2x5 = array_1d.reshape(2, 5)
array_2d = array_1d.reshape(1, -1) # -1 quer dizer "infinito"

print(array_1d)
print(array_2x5)