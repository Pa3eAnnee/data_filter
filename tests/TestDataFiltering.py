import csv
import os
import unittest
import json
import yaml
from src.data_filtering import filter_data, compare_values, compare_string, compare_numeric, compare_boolean, compare_list
from src.user_interface import save_filtered_results
import xml.etree.ElementTree as ET

class TestDataFiltering(unittest.TestCase):

    def setUp(self):
        self.test_data = [
            {"name": "Alice", "age": 30, "is_student": True, "grades": [85, 90, 95]},
            {"name": "Bob", "age": 25, "is_student": False, "grades": [70, 75, 80]},
            {"name": "Charlie", "age": 35, "is_student": True, "grades": [95, 100, 90]},
            {"name": "David", "age": 40, "is_student": False, "grades": [60, 65, 70]}
        ]

    def test_filter_string_equal(self):
        result = filter_data(self.test_data, [("name", "equal_to", "Alice")])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "Alice")

    def test_filter_string_contains(self):
        result = filter_data(self.test_data, [("name", "contains", "li")])
        self.assertEqual(len(result), 2)
        self.assertIn("Alice", [item["name"] for item in result])
        self.assertIn("Charlie", [item["name"] for item in result])

    def test_filter_numeric_greater_than(self):
        result = filter_data(self.test_data, [("age", "greater_than", 30)])
        self.assertEqual(len(result), 2)
        self.assertTrue(all(item["age"] > 30 for item in result))

    def test_filter_numeric_range(self):
        result = filter_data(self.test_data, [("age", "range", (25, 35))])
        self.assertEqual(len(result), 3)
        self.assertTrue(all(25 <= item["age"] <= 35 for item in result))

    def test_filter_boolean(self):
        result = filter_data(self.test_data, [("is_student", "equal_to", "true")])
        self.assertEqual(len(result), 2)
        self.assertTrue(all(item["is_student"] for item in result))

    def test_filter_list_length(self):
        result = filter_data(self.test_data, [("grades", "length_greater_than", 2)])
        self.assertEqual(len(result), 4)  # All items have 3 grades

    def test_filter_list_contains(self):
        result = filter_data(self.test_data, [("grades", "contains", 100)])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "Charlie")

    def test_multiple_filters(self):
        result = filter_data(self.test_data, [
            ("age", "greater_than", 30),
            ("is_student", "equal_to", "true")
        ])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "Charlie")

    def test_no_results(self):
        result = filter_data(self.test_data, [("age", "greater_than", 100)])
        self.assertEqual(result, "No results...")

    def test_invalid_field(self):
        result = filter_data(self.test_data, [("invalid_field", "equal_to", "value")])
        self.assertEqual(result, "No results...")

    def test_compare_string_case_insensitive(self):
        self.assertTrue(compare_string("Alice", "contains", "LI"))
        self.assertTrue(compare_string("alice", "equal_to", "ALICE"))

    def test_compare_numeric_edge_cases(self):
        self.assertTrue(compare_numeric(10, "equal_to", 10.0))
        self.assertFalse(compare_numeric(10, "greater_than", 10))
        self.assertTrue(compare_numeric(10, "greater_than_or_equal_to", 10))

    def test_compare_boolean_edge_cases(self):
        self.assertTrue(compare_boolean(True, "equal_to", "true"))
        self.assertTrue(compare_boolean(False, "equal_to", "FALSE"))

    def test_compare_list_edge_cases(self):
        self.assertTrue(compare_list([1, 2, 3], "length_equal_to", 3))
        self.assertTrue(compare_list([1, 2, 3], "contains", "2"))
        self.assertFalse(compare_list([], "contains", "value"))

    def test_regex_filter(self):
        result = filter_data(self.test_data, [("name", "regex", ".*ar.*")])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'Charlie')

    def test_regex_filter_no_match(self):
        result = filter_data(self.test_data, [("name", "regex", ".*xy.*")])
        self.assertEqual(result, "No results...")

    def test_string_equal_to(self):
        result = filter_data(self.test_data, [("name", "equal_to", "Alice")])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'Alice')

    def test_string_contains(self):
        result = filter_data(self.test_data, [("name", "contains", "ob")])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'Bob')

    def test_string_starts_with(self):
        result = filter_data(self.test_data, [("name", "starts_with", "Da")])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'David')

    def test_string_ends_with(self):
        result = filter_data(self.test_data, [("name", "ends_with", "ie")])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'Charlie')

    def test_lexicographically_greater_than(self):
        result = filter_data(self.test_data, [("name", "lexicographically_greater_than", "C")])
        self.assertEqual(len(result), 2)
        self.assertIn(result[0]['name'], ['Charlie', 'David'])
        self.assertIn(result[1]['name'], ['Charlie', 'David'])

    def test_lexicographically_less_than(self):
        result = filter_data(self.test_data, [("name", "lexicographically_less_than", "C")])
        self.assertEqual(len(result), 2)
        self.assertIn(result[0]['name'], ['Alice', 'Bob'])
        self.assertIn(result[1]['name'], ['Alice', 'Bob'])

    def test_case_insensitive_comparison(self):
        result = filter_data(self.test_data, [("name", "equal_to", "aLiCe")])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'Alice')

    def test_compare_string_regex(self):
        self.assertTrue(compare_string("Charlie", "regex", ".*ar.*"))
        self.assertFalse(compare_string("David", "regex", ".*ar.*"))

    def test_numeric_greater_than(self):
        result = filter_data(self.test_data, [("age", "greater_than", 30)])
        self.assertEqual(len(result), 2)
        self.assertIn(result[0]['name'], ['Charlie', 'David'])
        self.assertIn(result[1]['name'], ['Charlie', 'David'])

    def test_boolean_filter(self):
        result = filter_data(self.test_data, [("is_student", "equal_to", "true")])
        self.assertEqual(len(result), 2)
        self.assertIn(result[0]['name'], ['Alice', 'Charlie'])
        self.assertIn(result[1]['name'], ['Alice', 'Charlie'])

    def test_list_contains(self):
        result = filter_data(self.test_data, [("grades", "contains", 100)])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'Charlie')

    def test_multiple_filters(self):
        result = filter_data(self.test_data, [
            ("age", "greater_than", 30),
            ("is_student", "equal_to", "true")
        ])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'Charlie')

    def test_save_filtered_results_json(self):
        filtered_data = filter_data(self.test_data, [("age", "greater_than", 30)])
        filename = "test_filtered_data.json"
        save_filtered_results(filtered_data, test_format="1", test_filename=filename)
        
        self.assertTrue(os.path.exists(filename))
        with open(filename, 'r') as f:
            saved_data = json.load(f)
        self.assertEqual(filtered_data, saved_data)
        os.remove(filename)

    def test_save_filtered_results_csv(self):
        filtered_data = filter_data(self.test_data, [("is_student", "equal_to", "true")])
        filename = "test_filtered_data.csv"
        save_filtered_results(filtered_data, test_format="2", test_filename=filename)
        
        self.assertTrue(os.path.exists(filename))
        with open(filename, 'r', newline='') as f:
            reader = csv.DictReader(f, delimiter=';')  # Specify the delimiter
            saved_data = list(reader)
        self.assertEqual(len(filtered_data), len(saved_data))
        self.assertEqual(set(filtered_data[0].keys()), set(saved_data[0].keys()))  # Use set for unordered comparison
        os.remove(filename)

    def test_save_filtered_results_xml(self):
        filtered_data = filter_data(self.test_data, [("name", "contains", "a")])
        filename = "test_filtered_data.xml"
        save_filtered_results(filtered_data, test_format="3", test_filename=filename)
        
        self.assertTrue(os.path.exists(filename))
        tree = ET.parse(filename)
        root = tree.getroot()
        saved_data = [child.attrib for child in root]
        self.assertEqual(len(filtered_data), len(saved_data))
        os.remove(filename)

    def test_save_filtered_results_yaml(self):
        filtered_data = filter_data(self.test_data, [("grades", "contains", 100)])
        filename = "test_filtered_data.yaml"
        save_filtered_results(filtered_data, test_format="4", test_filename=filename)
        
        self.assertTrue(os.path.exists(filename))
        with open(filename, 'r') as f:
            saved_data = yaml.safe_load(f)
        self.assertEqual(filtered_data, saved_data)
        os.remove(filename)

    def test_save_filtered_results_no_data(self):
        filtered_data = "No results..."
        result = save_filtered_results(filtered_data)
        self.assertIsNone(result)

    def test_save_filtered_results_invalid_choice(self):
        filtered_data = filter_data(self.test_data, [("age", "greater_than", 30)])
        result = save_filtered_results(filtered_data, test_format="5", test_filename="invalid.txt")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()