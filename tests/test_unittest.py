import unittest
from Utils import load_json

class TestCalc(unittest.TestCase):
    def test_unittest(self):
        self.assertRaises(FileNotFoundError, load_json("operations.json"), load_json('random'))