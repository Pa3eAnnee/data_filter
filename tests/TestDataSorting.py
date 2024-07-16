import unittest
from unittest.mock import patch
from io import StringIO
from src.data_sorting import (
    get_available_fields, display_available_fields, get_sort_fields,
    get_sort_orders, sort_data, display_sorted_data
)

class TestDataSorting(unittest.TestCase):

    def setUp(self):
        self.test_data = [
            {"name": "Alice", "age": 30, "score": 85},
            {"name": "Bob", "age": 25, "score": 92},
            {"name": "Charlie", "age": 35, "score": 78},
            {"name": "David", "age": 28, "score": 95}
        ]

    def test_get_available_fields(self):
        fields = get_available_fields(self.test_data)
        self.assertEqual(fields, ["name", "age", "score"])

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_available_fields(self, mock_stdout):
        fields = ["name", "age", "score"]
        display_available_fields(fields)
        expected_output = "Available fields for sorting:\n1. name\n2. age\n3. score\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['1', '2', '0'])
    def test_get_sort_fields(self, mock_input):
        fields = ["name", "age", "score"]
        sort_fields = get_sort_fields(fields)
        self.assertEqual(sort_fields, ["name", "age"])

    @patch('builtins.input', side_effect=['a', 'd'])
    def test_get_sort_orders(self, mock_input):
        sort_fields = ["name", "age"]
        order_choices = get_sort_orders(sort_fields)
        self.assertEqual(order_choices, [False, True])

    @patch('builtins.input', side_effect=['1', '2', '0', 'a', 'd'])
    def test_sort_data(self, mock_input):
        result = sort_data(self.test_data)
        expected_order = ['Alice', 'Bob', 'Charlie', 'David']
        self.assertEqual([item['name'] for item in result], expected_order)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_sorted_data(self, mock_stdout):
        sorted_data = [
            {"name": "Alice", "age": 30, "score": 85},
            {"name": "Bob", "age": 25, "score": 92}
        ]
        display_sorted_data(sorted_data)
        expected_output = "{'name': 'Alice', 'age': 30, 'score': 85}\n{'name': 'Bob', 'age': 25, 'score': 92}\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()