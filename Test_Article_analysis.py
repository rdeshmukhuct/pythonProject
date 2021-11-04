import unittest
from article_analysis import GUIFunctions


class MyTestCase(unittest.TestCase):
    f = GUIFunctions()
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_get_article_length(self):
        assert GUIFunctions.get_article_length()

if __name__ == '__main__':
    unittest.main()
