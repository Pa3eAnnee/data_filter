import unittest
from unittest.mock import patch
from src.data_sorting import sort_data

class TestDataSorting(unittest.TestCase):

    def setUp(self):
        self.test_data = [
            {"name": "Alice", "age": 30, "score": 85},
            {"name": "Bob", "age": 25, "score": 92},
            {"name": "Charlie", "age": 35, "score": 78},
            {"name": "David", "age": 28, "score": 95}
        ]

    @patch('builtins.input', side_effect=['1', '0', 'a'])
    def test_sort_by_name(self, mock_input):
        result = sort_data(self.test_data)
        self.assertEqual([item['name'] for item in result], ['Alice', 'Bob', 'Charlie', 'David'])

    @patch('builtins.input', side_effect=['2', 'd'])
    def test_sort_by_age_descending(self, mock_input):
        result = sort_data(self.test_data)
        actual_order = [item['name'] for item in result]
        expected_order = ['Charlie', 'Alice', 'David', 'Bob']
        print("\ntest_sort_by_age_descending:")
        print(f"Actual order: {actual_order}")
        print(f"Expected order: {expected_order}")
        print(f"Actual ages: {[item['age'] for item in result]}")
        self.assertEqual(actual_order, expected_order)

    @patch('builtins.input', side_effect=['3', 'a'])
    def test_sort_by_score(self, mock_input):
        result = sort_data(self.test_data)
        actual_order = [item['name'] for item in result]
        expected_order = ['Charlie', 'Alice', 'Bob', 'David']
        print("\ntest_sort_by_score:")
        print(f"Actual order: {actual_order}")
        print(f"Expected order: {expected_order}")
        print(f"Actual scores: {[item['score'] for item in result]}")
        self.assertEqual(actual_order, expected_order)
        
    def test_sort_empty_data(self):
        with patch('builtins.input', side_effect=['1', 'a']):
            result = sort_data([])
        self.assertEqual(result, "No data to sort")

    @patch('builtins.input', side_effect=['1', '0', 'a'])
    def test_sort_single_item(self, mock_input):
        single_item = [{"name": "Alice", "age": 30, "score": 85}]
        result = sort_data(single_item)
        self.assertEqual(result, single_item)

    @patch('builtins.input', side_effect=['2', 'a', '1', 'a'])
    def test_sort_multiple_fields(self, mock_input):
        result = sort_data(self.test_data)
        actual_order = [item['name'] for item in result]
        expected_order = ['Bob', 'David', 'Alice', 'Charlie']
        print("\ntest_sort_multiple_fields:")
        print(f"Actual order: {actual_order}")
        print(f"Expected order: {expected_order}")
        self.assertEqual(actual_order, expected_order)

    @patch('builtins.input', side_effect=['4'])
    def test_sort_invalid_field(self, mock_input):
        result = sort_data(self.test_data)
        self.assertEqual(result, self.test_data)
    
    @patch('builtins.input', side_effect=['2', 'a'])
    def test_sort_by_age(self, mock_input):
        result = sort_data(self.test_data)
        actual_order = [item['name'] for item in result]
        expected_order = ['Bob', 'David', 'Alice', 'Charlie']
        print("\ntest_sort_by_age:")
        print(f"Actual order: {actual_order}")
        print(f"Expected order: {expected_order}")
        print(f"Actual ages: {[item['age'] for item in result]}")
        self.assertEqual(actual_order, expected_order)

if __name__ == '__main__':
    unittest.main()