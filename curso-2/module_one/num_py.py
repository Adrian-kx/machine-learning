import numpy as np

lista = [1, 2, 3, 4, 5]

array = np.array(lista)

print(array)
print(array.dtype)
print(array.shape)


# Abaixo ele cria um array que vai iniciar no 0,
# vai ter 5 elementos e termina no 10
array_linear = np.linspace(0, 10, 5)


print(array_linear)