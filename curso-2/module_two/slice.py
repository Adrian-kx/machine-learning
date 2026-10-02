import numpy as np

array_2d = np.array([[0, 1, 2, 3, 4],
                    [5, 6, 7, 8, 9],
                    [10, 11, 12, 13, 14]])

array_with_step = array_2d[1, ::2]
print(array_with_step)

array_with_all_steps = array_2d[1, 0:4:2]
print(array_with_all_steps)