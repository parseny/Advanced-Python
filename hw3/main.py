import numpy as np
from hw3.matrix import Matrix
from hw3.np_matrix import Matrix as Matrix_np

a = Matrix(list(np.random.randint(0, 10, (10, 10))))
b = Matrix(list(np.random.randint(0, 10, (10, 10))))

a_add_b = a + b
a_mul_b = a * b
a_b = a @ b

print(f"A:\n{a}")
print(f"B:\n{b}")

print(f"A+B:\n{a_add_b}")
print(f"A*B:\n{a_mul_b}")
print(f"A@B:\n{a_b}")

a = Matrix_np(list(np.random.randint(0, 10, (10, 10))))
b = Matrix_np(list(np.random.randint(0, 10, (10, 10))))

dir_ = 'artefacts/3.2/'
for i, path in enumerate(['matrix+.txt', 'matrix_mul.txt', 'matrix_matmul.txt']):
    path = dir_ + path
    if i == 0:
        c = a + b
    if i == 1:
        c = a * b
    if i == 2:
        c = a @ b
    c.save(path)

