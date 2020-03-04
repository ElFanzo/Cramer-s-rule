from unittest import main, TestCase

from cramers_rule import arr_remove, arr_replace_column, get_det, solve


class TestSolve(TestCase):
    def test_correct_array(self):
        arr_a = [
            [2, 5, 4],
            [1, 3, 2],
            [2, 10, 9],
        ]
        arr_b = [30, 150, 110]
        self.assertListEqual(solve(arr_a, arr_b), [-152, 270, -254])

        arr_a = [
            [1, -1],
            [3, 2],
        ]
        arr_b = [7, 16]
        self.assertListEqual(solve(arr_a, arr_b), [6, -1])

        arr_a = [
            [2, -4, 1, -5],
            [4, -7, -1, -8],
            [10, -18, 2, -23],
            [2, -3, 1, -1],
        ]
        arr_b = [2, -5, 3, 0]
        self.assertListEqual(solve(arr_a, arr_b), [1, 2, 3, -1])

        arr_a = [2]
        arr_b = [14]
        self.assertListEqual(solve(arr_a, arr_b), [7])

    def test_empty_array(self):
        with self.assertRaises(ValueError):
            solve([], [])

    def test_wrong_size_array(self):
        arr_a = [2]
        arr_b = [14, 4]
        with self.assertRaises(ValueError):
            solve(arr_a, arr_b)

        arr_a = [
            [1, 4],
            [5, 10],
        ]
        arr_b = [6, 5, 0]
        with self.assertRaises(ValueError):
            solve(arr_a, arr_b)

        arr_a = [
            [1, 4],
            [5, 10],
            [4, 6, 8],
        ]
        arr_b = [6, 5, 0]
        with self.assertRaises(ValueError):
            solve(arr_a, arr_b)

    def test_non_quadratic_array(self):
        arr_a = [
            [1, 5],
            [13, 60],
            [14, 0],
        ]
        arr_b = [15, 17]
        with self.assertRaises(ValueError):
            solve(arr_a, arr_b)

        arr_a = [4, 6, 8]
        arr_b = [6, 5, 0]
        with self.assertRaises(ValueError):
            solve(arr_a, arr_b)

    def test_array_with_zero_determinant(self):
        arr_a = [
            [1, -2],
            [-2, 4],
        ]
        arr_b = [6, 0]
        with self.assertRaises(ValueError):
            solve(arr_a, arr_b)


class TestArrReplaceColumn(TestCase):
    def setUp(self) -> None:
        self.arr_a = [
            [2, 5, 4],
            [1, 3, 2],
            [2, 10, 9],
        ]
        self.arr_b = [30, 150, 110]

    def test_array(self):
        self.assertListEqual(
            arr_replace_column(self.arr_a, self.arr_b, 0),
            [
                [30, 5, 4],
                [150, 3, 2],
                [110, 10, 9],
            ]
        )
        self.assertListEqual(
            arr_replace_column(self.arr_a, self.arr_b, 1),
            [
                [2, 30, 4],
                [1, 150, 2],
                [2, 110, 9],
            ]
        )
        self.assertListEqual(
            arr_replace_column(self.arr_a, self.arr_b, 2),
            [
                [2, 5, 30],
                [1, 3, 150],
                [2, 10, 110],
            ]
        )

    def test_single_array(self):
        arr_a = [2]
        arr_b = [3]
        self.assertListEqual(arr_replace_column(arr_a, arr_b, 0), [3])

    def test_negative_index(self):
        self.assertListEqual(
            arr_replace_column(self.arr_a, self.arr_b, -1),
            [
                [2, 5, 30],
                [1, 3, 150],
                [2, 10, 110],
            ]
        )

    def test_wrong_index(self):
        with self.assertRaises(IndexError):
            arr_replace_column(self.arr_a, self.arr_b, 3)


class TestArrRemove(TestCase):
    def setUp(self) -> None:
        self.arr = [
            [2, 5, 4],
            [1, 3, 2],
            [2, 10, 9],
        ]

    def test_array(self):
        self.assertListEqual(
            arr_remove(self.arr, 0),
            [
                [3, 2],
                [10, 9],
            ]
        )
        self.assertListEqual(
            arr_remove(self.arr, 1),
            [
                [1, 2],
                [2, 9],
            ]
        )
        self.assertListEqual(
            arr_remove(self.arr, 2),
            [
                [1, 3],
                [2, 10],
            ]
        )

    def test_tetra_array(self):
        arr = [
            [3, 4],
            [6, 7]
        ]
        self.assertListEqual(arr_remove(arr, 0), [7])
        self.assertListEqual(arr_remove(arr, 1), [6])

    def test_negative_index(self):
        self.assertListEqual(
            arr_remove(self.arr, -1),
            [
                [1, 3],
                [2, 10],
            ]
        )

    def test_wrong_index(self):
        with self.assertRaises(IndexError):
            arr_remove(self.arr, 3)


class TestGetDet(TestCase):
    def test_array(self):
        arr = [
            [2, 5, 4],
            [1, 3, 2],
            [2, 10, 9],
        ]
        self.assertEqual(get_det(arr), 5)

        arr = [
            [1, 1],
            [3, 2],
        ]
        self.assertEqual(get_det(arr), -1)

        arr = [
            [2, -4, 1, -5],
            [4, -7, -1, -8],
            [10, -18, 2, -23],
            [2, -3, 1, -1],
        ]
        self.assertEqual(get_det(arr), 24)

    def test_single_array(self):
        arr = [2]
        self.assertEqual(get_det(arr), 2)

    def test_array_with_zero_determinant(self):
        arr = [
            [1, -2],
            [-2, 4],
        ]
        self.assertEqual(get_det(arr), 0)


if __name__ == "__main__":
    main()
