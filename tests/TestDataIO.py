import unittest
from src.data_io import read_csv


class TestDataIO(unittest.TestCase):
    def test_read_csv(self):
        data = read_csv("data/test.csv")
        self.assertEqual(data[0]["firstname"], "John")
        self.assertEqual(data[0]["lastname"], "Doe")
        self.assertEqual(data[0]["age"], 25)
        self.assertEqual(data[0]["apprentice"], True)
        self.assertEqual(data[0]["grades"], [85, 90, 95])


if __name__ == "__main__":
    unittest.main()
