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

if __name__ == '__main__':
    unittest.main()