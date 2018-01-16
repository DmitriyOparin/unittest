# -*- coding: utf-8 -*-
'''
Module for text statistics calculation.
'''
import sys
import collections
import re

def get_char_frequencies(text):
    result ={}
    for char in text:
        if char in result:
          result[char]+=1
        else:
          result[char]=1
    return result

def get_unique_words(text):
    result = set()
    text = re.sub(r'[^\w\s]','',text).lower()
    for word in text.split(' '):
        result.add(word)
    if ' ' in result:
        result.remove(' ')
    if '' in result:
        result.remove('')
    return result

def main():
    print(get_char_frequencies(u"abc"))
    return 0
if __name__ == '__main__':
    status = main()    sys.exit(status)
