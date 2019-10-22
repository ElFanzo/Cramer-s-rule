from copy import deepcopy


class Cramer:
    """
    Solve SLAE using Cramer's rule.
    """

    @staticmethod
    def solve(arr_a, arr_b):
        """
        Find the solution of the SLAE.
        :param arr_a: The coefficient matrix of equations
        :param arr_b: The column vector of right-hand-sides of equations
        :return: X, the solution vector
        """
        if not (arr_a and arr_b):
            raise ValueError(
                "The matrix or the column vector of right-hand-sides of the "
                "equations is empty!"
            )

        size = len(arr_a)
        if len(arr_b) != size:
            raise ValueError(
                "The size of the column vector of right-hand-sides of the "
                "equations must be equal to the size of the matrix!"
            )

        if size != 1:
            for arr in arr_a:
                if len(arr) != size:
                    raise ValueError("The matrix is not quadratic!")

        det = Cramer.get_det(arr_a, size)
        if not det:
            raise ValueError("The matrix determinant must not be 0!")

        arr_x = [
            Cramer.get_det(Cramer.arr_replace(arr_a, arr_b, i), size) / det
            for i in range(size)
        ]

        return arr_x

    @staticmethod
    def get_det(arr, size):
        """
        Get the determinant of an array.
        :param arr: An array
        :param size: The size of an array
        :return: The array determinant
        """
        if size == 1:
            return arr[0]

        det = 0
        for i, j in enumerate(arr[0]):
            det += j * ((-1) ** i) * Cramer.get_det(
                Cramer.arr_remove(arr, i), size - 1
                )

        return det

    @staticmethod
    def arr_remove(arr, index):
        """
        Remove the 1st row and the index-th column from an array.
        :param arr: An array
        :param index: An index
        :return: A changed copy of the array
        """
        res = deepcopy(arr[1:])

        for i in res:
            i.pop(index)

        if len(res) == 1:
            return res[0]
        return res

    @staticmethod
    def arr_replace(arr, col, index):
        """
        Replace the index-th column from an array by a column vector of
        right-hand-sides of equations.
        :param arr: An array
        :param col: A column vector
        :param index: An index
        :return: A changed copy of the array
        """
        if len(arr) == 1:
            return col

        res = deepcopy(arr)

        for i, j in enumerate(col):
            res[i][index] = j

        return res
