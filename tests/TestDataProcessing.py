import unittest

from src.data_io import read_file
from src.data_processing import process_file

class TestDataProcessing(unittest.TestCase):
    def test_process_file_short(self):
        raw_data = read_file("data/test_data_short.csv")
        data = process_file(raw_data)
        self.assertEqual(data[0]["firstname"], "John")
        self.assertEqual(data[0]["lastname"], "Doe")
        self.assertEqual(data[0]["age"], "25")
        self.assertEqual(data[0]["apprentice"], "True")
        self.assertEqual(data[0]["grades"], "[85,90,95]")

    def test_process_file(self):
        raw_data = read_file("data/test_data.csv")
        data = process_file(raw_data)
        self.assertEqual(data[0]["firstname"], "John")
        self.assertEqual(data[0]["lastname"], "Doe")
        self.assertEqual(data[0]["age"], "25")
        self.assertEqual(data[0]["apprentice"], "True")
        self.assertEqual(data[0]["grades"], "[85,90,95]")
        self.assertEqual(data[1]["firstname"], "Jane")

if __name__ == "__main__":
    unittest.main()