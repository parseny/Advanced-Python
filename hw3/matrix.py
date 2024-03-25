class Matrix:
    def __init__(self, matrix: list[list]):
        self.matrix = matrix
        self.n_rows = len(matrix)
        self.n_cols = len(matrix[0])

    def __add__(self, other):
        if other.n_rows != self.n_rows or other.n_cols != self.n_cols:
            raise ValueError("Matrices must have the same shape")
        ans = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.n_cols)] for i in
               range(self.n_rows)]
        return Matrix(ans)

    def __sub__(self, other):
        if other.n_rows != self.n_rows or other.n_cols != self.n_cols:
            raise ValueError("Matrices must have the same shape")
        ans = [[self.matrix[i][j] - other.matrix[i][j] for j in range(self.n_cols)] for i in
               range(self.n_rows)]
        return Matrix(ans)

    def __mul__(self, other):
        if other.n_rows != self.n_rows or other.n_cols != self.n_cols:
            raise ValueError("Matrices must have the same shape")
        ans = [[self.matrix[i][j] * other.matrix[i][j] for j in range(self.n_cols)] for i in
               range(self.n_rows)]
        return Matrix(ans)

    def __matmul__(self, other):
        n_rows_other = other.n_rows
        n_cols_other = other.n_cols
        if n_rows_other != self.n_cols:
            raise ValueError("Matrices must have the same shape")
        ans = [[None] * n_cols_other for _ in range(self.n_rows)]
        for i in range(self.n_rows):
            for j in range(n_cols_other):
                ans[i][j] = sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.n_cols))
        return Matrix(ans)

    def __str__(self):
        max_width = max(len(str(item)) for row in self.matrix for item in row)
        formatted_matrix = '[[' + ']\n ['.join(
            ' '.join(f'{item:>{max_width}}' for item in row) for row in self.matrix) + ']]'
        return formatted_matrix
