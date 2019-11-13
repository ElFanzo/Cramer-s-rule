from unittest import main, TestCase

from cramers_rule import Cramer


class TestCramer(TestCase):
    def test_solve(self):
        arr_a = [
            [2, 5, 4],
            [1, 3, 2],
            [2, 10, 9],
        ]
        arr_b = [30, 150, 110]
        self.assertListEqual(Cramer.solve(arr_a, arr_b), [-152, 270, -254])

        arr_a = [
            [1, -1],
            [3, 2],
        ]
        arr_b = [7, 16]
        self.assertListEqual(Cramer.solve(arr_a, arr_b), [6, -1])

        arr_a = [
            [2, -4, 1, -5],
            [4, -7, -1, -8],
            [10, -18, 2, -23],
            [2, -3, 1, -1],
        ]
        arr_b = [2, -5, 3, 0]
        self.assertListEqual(Cramer.solve(arr_a, arr_b), [1, 2, 3, -1])

        arr_a = [
            [2, 5, 4],
            [1, 3, 2],
            [2, 10, 9],
        ]
        arr_b = [30, 150, 110]
        self.assertListEqual(Cramer.solve(arr_a, arr_b), [-152, 270, -254])

        arr_a = [2]
        arr_b = [14]
        self.assertListEqual(Cramer.solve(arr_a, arr_b), [7])

        with self.assertRaises(ValueError):
            Cramer.solve([], [])

        arr_a = [2]
        arr_b = [14, 4]
        with self.assertRaises(ValueError):
            Cramer.solve(arr_a, arr_b)

        arr_a = [
            [1, 4],
            [5, 10],
        ]
        arr_b = [6, 5, 0]
        with self.assertRaises(ValueError):
            Cramer.solve(arr_a, arr_b)

        arr_a = [
            [1, 4],
            [5, 10],
            [4, 6, 8],
        ]
        arr_b = [6, 5, 0]
        with self.assertRaises(ValueError):
            Cramer.solve(arr_a, arr_b)

        arr_a = [
            [1, -2],
            [-2, 4],
        ]
        arr_b = [6, 0]
        with self.assertRaises(ValueError):
            Cramer.solve(arr_a, arr_b)


if __name__ == "__main__":
    main()
