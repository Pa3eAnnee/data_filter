import unittest
import os

from src.data_io import read_file
from src.data_processing import process_file

class TestDataProcessing(unittest.TestCase):
    def setUp(self):
        self.base_path = "C:\\PA\\python\\data_filter\\tests\\data"

    def test_process_file_short_csv(self):
        data = process_file(os.path.join(self.base_path, "test_data_short.csv"))
        self.assertEqual(data[0]["firstname"], "John")
        self.assertEqual(data[0]["lastname"], "Doe")
        self.assertEqual(data[0]["age"], 25)
        self.assertEqual(data[0]["apprentice"], True)
        self.assertEqual(data[0]["grades"], "[85,90,95]")

    def test_process_file_csv(self):
        data = process_file(os.path.join(self.base_path, "test_data.csv"))
        self.assertEqual(data[0]["firstname"], "John")
        self.assertEqual(data[0]["lastname"], "Doe")
        self.assertEqual(data[0]["age"], 25)
        self.assertEqual(data[0]["apprentice"], True)
        self.assertEqual(data[0]["grades"], "[85,90,95]")
        self.assertEqual(data[1]["firstname"], "Jane")

    def test_process_file_short_xml(self):
        data = process_file(os.path.join(self.base_path, "test_data_short.xml"))
        self.assertEqual(data[0]["firstname"], "John")
        self.assertEqual(data[0]["lastname"], "Doe")
        self.assertEqual(data[0]["age"], 25)
        self.assertEqual(data[0]["apprentice"], True)
        self.assertEqual(data[0]["grades"], "[85,90,95]")

    def test_process_file_xml(self):
        data = process_file(os.path.join(self.base_path, "test_data.xml"))
        self.assertEqual(data[0]["firstname"], "John")
        self.assertEqual(data[0]["lastname"], "Doe")
        self.assertEqual(data[0]["age"], 25)
        self.assertEqual(data[0]["apprentice"], True)
        self.assertEqual(data[0]["grades"], "[85,90,95]")
        self.assertEqual(data[1]["firstname"], "Jane")

if __name__ == "__main__":
    unittest.main()