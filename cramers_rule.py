from copy import deepcopy


class CramersRule:
    @staticmethod
    def solve(arr_a, arr_b):
        if not (arr_a and arr_b):
            raise ValueError("The matrix or the column vector of right-hand-sides of the equations is empty!")

        size = len(arr_a)
        if len(arr_b) != size:
            raise ValueError("The size of the column vector of right-hand-sides of the equations must be equal to the "
                             "size of the matrix!")

        if size != 1:
            for arr in arr_a:
                if len(arr) != size:
                    raise ValueError("The matrix is not quadratic!")

        det = CramersRule.get_det(arr_a, size)
        if not det:
            raise ValueError("The matrix determinant must not be 0!")

        arr_x = [CramersRule.get_det(CramersRule.arr_replace(arr_a, arr_b, i), size) / det for i in range(size)]

        return arr_x

    @staticmethod
    def get_det(arr, size):
        if size == 1:
            return arr[0]

        #if size == 2:
        #    return CramersRule.get_det_2(arr)

        det = 0
        for i, j in enumerate(arr[0]):
            det += j * ((-1) ** i) * CramersRule.get_det(CramersRule.arr_remove(arr, i), size - 1)

        return det

    @staticmethod
    def get_det_2(arr):
        return arr[0][0] * arr[1][1] - arr[0][1] * arr[1][0]

    @staticmethod
    def arr_remove(arr, index):
        res = deepcopy(arr[1:])

        for i in res:
            i.pop(index)

        if len(res) == 1:
            return res[0]
        return res

    @staticmethod
    def arr_replace(arr, col, index):
        if len(arr) == 1:
            return col

        res = deepcopy(arr)

        for i, j in enumerate(col):
            res[i][index] = j

        return res
