import numpy as np

array_2d = np.array(
    [
        [0, 1],
        [3, 4],
        [5, 6],
    ]
)

# sem o apram axis ele soma tudo
# 0 soma as colunas
# 1 soma as linhas
sum = array_2d.sum() 
sum1 = array_2d.sum(axis=0) 
sum2 = array_2d.sum(axis=1) 

print(sum)
print(sum1)
print(sum2)