import unittest
from src.data_io import read_file


class TestDataIO(unittest.TestCase):
    def test_read_csv(self):
        data = read_file("data/test_data_short.csv")
        self.assertEqual(data, "firstname;lastname;age;apprentice;grades\nJohn;Doe;25,True;[85,90,95]")


if __name__ == "__main__":
    unittest.main()
