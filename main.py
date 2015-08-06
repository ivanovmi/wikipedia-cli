#!/usr/bin/env python
# -- coding: utf-8 --

__author__ = 'michael'

import wikipedia.wikipedia as wikipedia
from pprint import PrettyPrinter


class MyPrettyPrinter(PrettyPrinter):
    """
    That class print results in CLI with russian charset
    """
    def format(self, object, context, maxlevels, level):
        if isinstance(object, unicode):
            return object.encode('utf8'), True, False
        return PrettyPrinter.format(self, object, context, maxlevels, level)


def find_lang(string):
    languages_set = wikipedia.languages()
    new_dict = dict(zip(languages_set.values(),
                        languages_set.keys()))
    for i in range(len(new_dict.keys())):
        if unicode(string, 'utf-8').lower() in new_dict.keys()[i].lower():
            pair = new_dict.keys()[i]+': '+new_dict.values()[i]
            MyPrettyPrinter().pprint(pair)
            #return 0
        #else:
        #    return 1


def main():
    choice = ''
    known_language = ''
    while choice.lower() not in ['y', 'yes', 'n', 'no']:
        choice = raw_input('Default language - English. You wanna to change this? [y/n]: ')
        if choice.lower() in ['yes', 'y']:
            known_language = raw_input('You know your language abbreviation? [y/n]: ')
            if known_language.lower() in ['no', 'n']:
                lang_abbreviation = raw_input('Enter a native language naming: ')
                find_lang(lang_abbreviation)
                wikipedia.set_lang(raw_input('Enter your choice: '))
                name = raw_input('Page for search: ')
                MyPrettyPrinter().pprint(wikipedia.summary(name))

if __name__ == '__main__':
    main()