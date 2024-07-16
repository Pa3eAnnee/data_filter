import unittest
from unittest.mock import patch
from io import StringIO
from src.data_sorting import sort_data

class TestDataSorting(unittest.TestCase):

    def setUp(self):
        self.test_data = [
            {"name": "Alice", "age": 30, "score": 85},
            {"name": "Bob", "age": 25, "score": 92},
            {"name": "Charlie", "age": 35, "score": 78},
            {"name": "David", "age": 28, "score": 95}
        ]

    def test_sort_by_name(self):
        with patch('builtins.input', side_effect=['1', 'a']):
            result = sort_data(self.test_data)
        expected = [
            {"name": "Alice", "age": 30, "score": 85},
            {"name": "Bob", "age": 25, "score": 92},
            {"name": "Charlie", "age": 35, "score": 78},
            {"name": "David", "age": 28, "score": 95}
        ]
        self.assertEqual(result, expected)

    def test_sort_by_age_descending(self):
        with patch('builtins.input', side_effect=['2', 'd']):
            result = sort_data(self.test_data)
        expected = [
            {"name": "Charlie", "age": 35, "score": 78},
            {"name": "Alice", "age": 30, "score": 85},
            {"name": "David", "age": 28, "score": 95},
            {"name": "Bob", "age": 25, "score": 92}
        ]
        self.assertEqual(result, expected)

    def test_sort_by_score(self):
        with patch('builtins.input', side_effect=['3', 'a']):
            result = sort_data(self.test_data)
        expected = [
            {"name": "Charlie", "age": 35, "score": 78},
            {"name": "Alice", "age": 30, "score": 85},
            {"name": "Bob", "age": 25, "score": 92},
            {"name": "David", "age": 28, "score": 95}
        ]
        self.assertEqual(result, expected)

    def test_sort_empty_data(self):
        with patch('builtins.input', side_effect=['1', 'a']):
            result = sort_data([])
        self.assertEqual(result, "No data to sort")

    def test_sort_single_item(self):
        single_item = [{"name": "Alice", "age": 30, "score": 85}]
        with patch('builtins.input', side_effect=['1', 'a']):
            result = sort_data(single_item)
        self.assertEqual(result, single_item)

    def test_sort_invalid_field(self):
        with patch('builtins.input', side_effect=['4', 'a']):
            result = sort_data(self.test_data)
        self.assertEqual(result, 'Invalid field choice')

if __name__ == '__main__':
    unittest.main()