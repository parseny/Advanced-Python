import numpy as np


class Matrix:
    def __init__(self, matrix):
        self._matrix = np.array(matrix)

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, matrix):
        self._matrix = np.array(matrix)

    def __add__(self, other):
        if self._matrix.shape != other.matrix.shape:
            raise ValueError("Matrices must have the same shape")
        return Matrix(self._matrix + other.matrix)

    def __sub__(self, other):
        if self._matrix.shape != other.matrix.shape:
            raise ValueError("Matrices must have the same shape")
        return Matrix(self._matrix - other.matrix)

    def __mul__(self, other):
        # if not isinstance(other, Matrix):
        #     return Matrix(self.matrix * other)
        if self.matrix.shape != other.matrix.shape:
            raise ValueError("Matrices must have the same shape")
        return Matrix(self._matrix * other.matrix)

    def __matmul__(self, other):
        if self.matrix.shape[1] != other.matrix.shape[0]:
            raise ValueError("Matrices must have the same shape")
        return Matrix(self._matrix @ other.matrix)

    def __str__(self):
        return np.array_str(self._matrix)

    def save(self, filepath):
        with open(filepath, 'w') as file:
            file.write(self._matrix.__str__())
