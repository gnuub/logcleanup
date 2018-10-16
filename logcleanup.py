#!/usr/bin/python

"""
Program to remove files that match stem and extension.
"""

import re
from os import listdir


def main():
    #dirobject = r'C:\Users\sookie\Projects\Samples\logs'
    diroject = r'C:\Users\ssaypras\projects\Sample'

    pattern = r'delete'
    regex = re.compile(pattern, re.IGNORECASE)

    for fnobject in listdir(diroject):
        for match in regex.finditer(fnobject):
            print(fnobject)

if __name__ == '__main__':
    main()
