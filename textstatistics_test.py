# -*- coding: utf-8 -*-
'''
Tests for textstatistics module
'''

import unittest
import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
sys.path.append(root_path)

import textstatistics


class Test(unittest.TestCase):
    def test_get_char_frequencies_empty(self):
        text = u''
        result = textstatistics.get_char_frequencies(text)
        expected = {}
        self.assertDictEqual(result, expected)

    def test_get_char_frequencies_uniform(self):
        text = u'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '
        result = textstatistics.get_char_frequencies(text)
        expected = {char: 1 for char in text}
        self.assertDictEqual(result, expected)

    def test_get_char_frequencies_simple_text(self):
        text = u'Не слушайте тех, кто говорит дурно о других и хорошо о вас.'
        result = textstatistics.get_char_frequencies(text)
        expected = {
                    u'Н': 1, 
                    u'е': 3, 
                    u' ': 11, 
                    u'с': 2, 
                    u'л': 1, 
                    u'у': 3, 
                    u'ш': 2, 
                    u'а': 2, 
                    u'й': 1, 
                    u'т': 4, 
                    u'х': 3, 
                    u',': 1, 
                    u'к': 1, 
                    u'о': 9,
                    u'г': 2, 
                    u'в': 2, 
                    u'р': 4, 
                    u'и': 3, 
                    u'д': 2, 
                    u'н': 1, 
                    u'.': 1,                      
                    }
        self.assertDictEqual(result, expected)

    def test_my_get_char(self):
        text = u'hello world!!!'
        result = textstatistics.get_char_frequencies(text)
        expected = {
                    u'h': 1, 
                    u'e': 1,
                    u'l': 3,
                    u'o': 2,
                    u' ': 1,
                    u'w': 1,
                    u'r': 1, 
                    u'd': 1, 
                    u'!': 3,                     
                    }
        self.assertDictEqual(result, expected)

    def test_get_unique_words_empty(self):
        text = u''
        result = textstatistics.get_unique_words(text)
        expected = set()
        self.assertSetEqual(result, expected)

    def test_get_unique_words_char(self):
        text = u'a a a a a b b c'
        result = textstatistics.get_unique_words(text)
        expected = set(['a', 'b', 'c'])
        self.assertSetEqual(result, expected)

    def test_get_unique_words_text(self):
        text = u'hey boy, hey girl'
        result = textstatistics.get_unique_words(text)
        expected = set(['hey', 'girl', 'boy'])
        self.assertSetEqual(result, expected)        

if __name__ == "__main__":
    unittest.main(verbosity=2)
