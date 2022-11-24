import unittest
from textfrommatrix import convert_to_text


class Testmethods(unittest.TestCase):

    def test_output1(self):
        example = [
            ["n", "x"],
            ["m", "o"]
        ]
        self.assertEqual(convert_to_text(example), "no")

    def test_output2(self):
        example2 = [
            ["h", "p", "e"],
            ["k", "l", "a"],
            ["l", "m", "o"]
        ]
        self.assertEqual(convert_to_text(example2), "hello")


if __name__ == '__main__':
    unittest.main()