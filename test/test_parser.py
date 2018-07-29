import unittest
import sys
sys.path.append('../')
from nlpy.parser import Parser


class TestParser(unittest.TestCase):
    def setUp(self):
        self.text = 'Hello, World! My name is Chris. What is your name?'
        self.p = Parser(self.text)

    def test_list_sentences(self):
        result = ['Hello, World', 'My name is Chris', 'What is your name']
        self.assertEqual(result, self.p.list_sentences())

    def test_list_words_flat(self):
        result = ['Hello', 'World', 'My', 'name', 'is', 'Chris', 'What', 'is', 'your', 'name']
        self.assertEqual(result, self.p.list_words(flat=True))

    def test_list_words_embedded(self):
        result = [['Hello', 'World'], ['My', 'name', 'is', 'Chris'], ['What', 'is', 'your', 'name']]
        self.assertEqual(result, self.p.list_words(flat=False))

    def test_list_words_counted(self):
        result = {'Hello':1, 'World':1, 'My':1, 'name':2, 'is':2, 'Chris':1, 'What':1, 'your':1}
        self.assertEqual(result, self.p.list_words(count=True))

if __name__ == '__main__':
    unittest.main()