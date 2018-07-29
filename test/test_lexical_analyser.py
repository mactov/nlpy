import unittest
import sys
sys.path.append('../')
from nlpy.parser import Parser


class TestParser(unittest.TestCase):
    def setUp(self):
        self.text = 'Hello, World! My name is Chris. What is your name?'
        self.p = Parser(self.text)