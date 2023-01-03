import asyncio
import unittest

from matrix.traverse_matrix import format_matrix, traverse_matrix, get_matrix

TRAVERSAL = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70
]

PREPARED_MATRIX = [[10, 20, 30, 40],
                   [50, 60, 70, 80],
                   [90, 100, 110, 120],
                   [130, 140, 150, 160]]

PREPARED_MATRIX2 = [[10, 20, 30],
                    [50, 60, 70],
                    [90, 100, 110]]

SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'


class TestFormatMatrix(unittest.TestCase):
    """Тестируем format_matrix."""

    def test_four_dim_matrix(self):
        with open("test_matrix.txt") as file:
            call = format_matrix(file.read())
        result = PREPARED_MATRIX
        self.assertEqual(
            call, result, 'Функция format_matrix не работает с 4ех размерной матрицей '
        )

    def test_three_dim_matrix(self):
        with open("test_matrix2.txt") as file:
            call = format_matrix(file.read())
        result = PREPARED_MATRIX2
        self.assertEqual(
            call, result, 'Функция format_matrix не работает с 3ех размерной матрицей '
        )

    def test_empty_str(self):
        call = format_matrix("")
        result = []
        self.assertEqual(
            call, result, 'Функция format_matrix не работает с пустой строкой'
        )


class TestTraverseMatrix(unittest.TestCase):
    """Тестируем traverse_matrix."""

    def test_traverse_matrix(self):
        call = traverse_matrix(PREPARED_MATRIX)
        result = TRAVERSAL
        self.assertEqual(
            call, result, 'Функция traverse_matrix не работает с правильной матрицей'
        )


class TestGetMatrix(unittest.TestCase):
    """Тестируем get_matrix."""

    def test_get_matrix(self):
        call = get_matrix(SOURCE_URL)
        result = TRAVERSAL
        self.assertEqual(
            call, result, 'Функция get_matrix не работает с урлом'
        )


if __name__ == '__main__':
    unittest.main()
