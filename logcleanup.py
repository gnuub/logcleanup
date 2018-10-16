#!/usr/bin/python3

"""
Program to remove files that match regex in given directory.
"""

import re
from os import listdir, remove
from sys import platform

def main():
    dirobject = r'C:\Users\ssaypras\projects\Sample'

    pattern = r'delete'
    regex = re.compile(pattern, re.IGNORECASE)

    for fnobject in listdir(dirobject):
        for match in regex.finditer(fnobject):
            if platform == 'win32'
                file = dirobject + '\\' + fnobject
                remove(file)
            elif platform == 'linux'
                file = dirobject + '/' + fnobject
                remove(file)
            else:
                raise ValueError('Unknown OS')

if __name__ == '__main__':
    main()
