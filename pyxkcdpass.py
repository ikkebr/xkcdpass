#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# xkcdpass
# http://danielmcgraw.github.io/xkcdpass/
#
# pyxkcdpass
# https://github.com/ikkebr/xkcdpass
#
# Generate passwords like Randall Munroe (http://xkcd.com/936/)
# Default dictionary from http://www.englishclub.com/vocabulary/common-words-5000.htm
#

import os
import random
import argparse


class XKCDPass(object):
    def __init__(self, dictionary='dictionary', length=4, readable=True, *args, **kwargs):
        self.dictionary = dictionary
        self.length = length
        self.separator = ""

        if readable:
            self.separator = " "

        
    def generate_random_password(self, length=None):
        with open(self.dictionary, 'r') as dictionary:
            possible_words = dictionary.readlines()
            return self.separator.join( map(str.strip, random.sample(possible_words, min(length or self.length, len(possible_words))) ))


def main():
    
    parser = argparse.ArgumentParser(description="Python tool that generates passwords like XKCD 936")

    default_dictionary = os.path.join(os.path.dirname(__file__), 'dictionary')

    parser.add_argument("--dictionary", dest="dictionary_path",
                      help="Specify a path to a dictionary", metavar="PATH", default=default_dictionary)

    parser.add_argument("--length", dest="password_length", type=int,
                      help="Specify the password length", metavar="LENGTH", default=4)

    parser.add_argument("--readable", dest="password_readable", help="Outputs a readable password", default=False, action='store_true')


    options = parser.parse_args()
    print(options)

    if options.password_length < 1:
        parser.error("Your password should contain at least 1 word.")

    if not os.path.isfile(options.dictionary_path):
        parser.error("I cannot find your dictionary file. Please make sure it is readable.")

    xkcdpass = XKCDPass(options.dictionary_path, options.password_length, options.password_readable)
    
    print(xkcdpass.generate_random_password())
    



if __name__ == "__main__":
    main()

