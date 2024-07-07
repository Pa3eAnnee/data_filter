import unittest

from src.data_io import read_file
from src.data_processing import process_file

class TestDataProcessing(unittest.TestCase):
    def test_process_file(self):
        raw_data = read_file("data/test_data_short.csv")
        data = process_file(raw_data)
        self.assertEqual(data["firstname"], "John")
        self.assertEqual(data["lastname"], "Doe")
        self.assertEqual(data["age"], "25")
        self.assertEqual(data["apprentice"], "True")
        self.assertEqual(data["grades"], "[85,90,95]")

if __name__ == "__main__":
    unittest.main()