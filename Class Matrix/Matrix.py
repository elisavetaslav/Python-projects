from copy import deepcopy
from sys import stdin


class MatrixError(BaseException):
    def __init__(self, m1, m2):
        self.matrix1 = m1
        self.matrix2 = m2


class Matrix:
    def __init__(self, a):
        self.a = deepcopy(a)
        self.n = len(a)
        self.m = len(a[0])

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, self.a[i])) for i in range(self.n)])

    def __add__(self, other):
        if self.n != other.n or self.m != other.m:
            raise MatrixError(self, other)
        res = []
        for i in range(self.n):
            row = []
            for j in range(self.m):
                row.append(self.a[i][j] + other.a[i][j])
            res.append(row)
        return Matrix(res)

    def __mul__(self, val):
        if isinstance(val, Matrix):
            if self.m != val.n:
                raise MatrixError(self, val)
            res = []
            for i in range(self.n):
                row = []
                for j in range(val.m):
                    x = 0
                    for k in range(self.m):
                        x += self.a[i][k] * val.a[k][j]
                    row.append(x)
                res.append(row)
            return Matrix(res)
        else:
            res = []
            for i in range(self.n):
                row = []
                for j in range(self.m):
                    row.append(val * self.a[i][j])
                res.append(row)
            return Matrix(res)

    __rmul__ = __mul__

    def transpose(self):
        res = []
        for i in range(self.m):
            row = [self.a[j][i] for j in range(self.n)]
            res.append(row)
        self.a = res
        self.n, self.m = self.m, self.n
        return self

    @staticmethod
    def transposed(self):
        res = []
        for i in range(self.m):
            row = [self.a[j][i] for j in range(self.n)]
            res.append(row)
        return Matrix(res)

    def swap_rows(self, i, j):
        self.a[i], self.a[j] = self.a[i], self.a[j]

    def add_rows(self, i, j, val):
        for k in range(self.m):
            self.a[i][k] += self.a[j][k] * val

    def mul_row(self, i, val):
        for j in range(self.m):
            self.a[i][j] *= val

    def solve(self, b):
        arr1 = []
        for i in range(self.n):
            arr1.append(self.a[i] + [b[i]])
        a1 = Matrix(arr1)

        for i in range(self.m):

            row_id = i
            for j in range(i, self.n):
                if abs(a1.a[j][i]) != 0:
                    row_id = j
                    break
            a1.swap_rows(row_id, i)
            a1.mul_row(i, 1 / a1.a[i][i])

            for j in range(i + 1, self.n):
                if a1.a[j][i] != 0:
                    val = - a1.a[j][i] / a1.a[i][i]
                    a1.add_rows(j, i, val)
        ans = [0] * self.n
        for i in range(self.m - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                if a1.a[j][i] != 0:
                    a1.add_rows(j, i, - (a1.a[j][i] / a1.a[i][i]))
        for i in range(self.n):
            ans[i] = a1.a[i][-1]
        return ans


class SquareMatrix(Matrix):

    def __pow__(self, val):
        if val == 0:
            res = []
            for i in range(self.n):
                row = []
                for j in range(self.m):
                    row = [0 * l for l in range(self.n)]
                res.append(row)
            for i in range(self.n):
                res[i][i] = 1
            return Matrix(res)
        else:
            if val % 2 == 0:
                val //= 2
                p = self ** val
                return p * p
            else:
                val -= 1
                return self * (self ** val)


exec(stdin.read())
