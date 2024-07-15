import math
import unittest
from src.data_statistics import identify_field_type, calculate_numeric_stats, calculate_boolean_stats, calculate_list_stats, calculate_stats

class TestDataStatistics(unittest.TestCase):

    def setUp(self):
        self.test_data = [
            {
                "name": "John Doe",
                "age": 30,
                "is_student": True,
                "grades": [85, 90, 95],
                "height": 1.75
            },
            {
                "name": "Jane Smith",
                "age": 25,
                "is_student": False,
                "grades": [80, 85, 90],
                "height": 1.68
            },
            {
                "name": "Bob Johnson",
                "age": 35,
                "is_student": True,
                "grades": [75, 80, 85],
                "height": 1.82
            }
        ]

    def test_identify_field_type(self):
        self.assertEqual(identify_field_type(["John Doe", "Jane Smith", "Bob Johnson"]), "string")
        self.assertEqual(identify_field_type([30, 25, 35]), "numeric")
        self.assertEqual(identify_field_type([True, False, True]), "boolean")
        self.assertEqual(identify_field_type([[85, 90, 95], [80, 85, 90], [75, 80, 85]]), "list")

    def test_calculate_numeric_stats(self):
        ages = [30, 25, 35]
        stats = calculate_numeric_stats(ages)
        self.assertEqual(stats["min"], 25)
        self.assertEqual(stats["max"], 35)
        self.assertEqual(stats["average"], 30)

    def test_calculate_boolean_stats(self):
        is_student = [True, False, True]
        stats = calculate_boolean_stats(is_student)
        self.assertAlmostEqual(stats["true_percentage"], 66.67, places=2)

    def test_calculate_list_stats(self):
        grades = [[85, 90, 95], [80, 85, 90], [75, 80, 85]]
        stats = calculate_list_stats(grades)
        self.assertEqual(stats["min_length"], 3)
        self.assertEqual(stats["max_length"], 3)
        self.assertEqual(stats["average_length"], 3)
        self.assertEqual(stats["total_length"], 9)
        self.assertEqual(stats["min_value"], 75)
        self.assertEqual(stats["max_value"], 95)
        self.assertAlmostEqual(stats["average_value"], 85, places=2)
        self.assertEqual(stats["total_items"], 9)

    def test_calculate_stats(self):
        stats = calculate_stats(self.test_data)
        
        self.assertEqual(stats["name"]["type"], "string")
        
        self.assertEqual(stats["age"]["min"], 25)
        self.assertEqual(stats["age"]["max"], 35)
        self.assertEqual(stats["age"]["average"], 30)
        
        self.assertAlmostEqual(stats["is_student"]["true_percentage"], 66.67, places=2)
        
        self.assertEqual(stats["grades"]["min_length"], 3)
        self.assertEqual(stats["grades"]["max_length"], 3)
        self.assertEqual(stats["grades"]["average_length"], 3)
        self.assertEqual(stats["grades"]["total_length"], 9)
        self.assertEqual(stats["grades"]["min_value"], 75)
        self.assertEqual(stats["grades"]["max_value"], 95)
        self.assertAlmostEqual(stats["grades"]["average_value"], 85, places=2)
        self.assertEqual(stats["grades"]["total_items"], 9)
        
        self.assertEqual(stats["height"]["min"], 1.68)
        self.assertEqual(stats["height"]["max"], 1.82)
        self.assertAlmostEqual(stats["height"]["average"], 1.75, places=2)


    def test_empty_data(self):
        empty_data = []
        stats = calculate_stats(empty_data)
        self.assertEqual(stats, {}, "Empty data should return empty statistics")

    def test_single_item_data(self):
        single_item_data = [{"name": "John", "age": 30, "is_student": True, "grades": [90]}]
        stats = calculate_stats(single_item_data)
        self.assertEqual(stats["name"]["type"], "string")
        self.assertEqual(stats["age"]["min"], 30)
        self.assertEqual(stats["age"]["max"], 30)
        self.assertEqual(stats["age"]["average"], 30)
        self.assertEqual(stats["is_student"]["true_percentage"], 100)
        self.assertEqual(stats["grades"]["min_length"], 1)
        self.assertEqual(stats["grades"]["max_length"], 1)
        self.assertEqual(stats["grades"]["average_length"], 1)
        self.assertEqual(stats["grades"]["min_value"], 90)
        self.assertEqual(stats["grades"]["max_value"], 90)
        self.assertEqual(stats["grades"]["average_value"], 90)

    def test_missing_values(self):
        data_with_missing = [
            {"name": "John", "age": 30, "grades": [80, 90]},
            {"name": "Jane", "grades": [70, 80, 90]},
            {"name": "Bob", "age": 25, "grades": []}
        ]
        stats = calculate_stats(data_with_missing)
        self.assertNotIn("is_student", stats, "Missing field should not appear in stats")
        self.assertEqual(stats["age"]["min"], 25, "Age stats should only consider available values")
        self.assertEqual(stats["age"]["max"], 30, "Age stats should only consider available values")
        self.assertEqual(stats["grades"]["min_length"], 0, "Should handle empty list")

    def test_mixed_types(self):
        mixed_data = [
            {"value": 10},
            {"value": "20"},
            {"value": True},
            {"value": [30, 40]}
        ]
        stats = calculate_stats(mixed_data)
        self.assertEqual(stats["value"]["type"], "string", "Mixed types should be treated as strings")

    def test_extreme_values(self):
        extreme_data = [
            {"age": 0, "score": float('inf')},
            {"age": 999, "score": float('-inf')},
            {"age": 50, "score": 1e20}
        ]
        stats = calculate_stats(extreme_data)
        self.assertEqual(stats["age"]["min"], 0)
        self.assertEqual(stats["age"]["max"], 999)
        self.assertTrue(math.isinf(stats["score"]["max"]))
        self.assertTrue(math.isinf(stats["score"]["min"]))

    def test_boolean_edge_cases(self):
        bool_data = [
            {"flag": True},
            {"flag": False},
            {"flag": "True"},
            {"flag": "FALSE"},
            {"flag": 1},
            {"flag": 0}
        ]
        stats = calculate_stats(bool_data)
        self.assertAlmostEqual(stats["flag"]["true_percentage"], 50, places=2)

    def test_list_edge_cases(self):
        list_data = [
            {"grades": []},
            {"grades": [1]},
            {"grades": [1, 2, 3, 4, 5]},
            {"grades": [100] * 1000}
        ]
        stats = calculate_stats(list_data)
        self.assertEqual(stats["grades"]["min_length"], 0)
        self.assertEqual(stats["grades"]["max_length"], 1000)
        self.assertEqual(stats["grades"]["min_value"], 1)
        self.assertEqual(stats["grades"]["max_value"], 100)


if __name__ == '__main__':
    unittest.main()