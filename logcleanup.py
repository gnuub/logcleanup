#!/usr/bin/python

"""
Program to remove files that match regex in given directory.
"""

import re
import argparse
from os import listdir, remove
from sys import platform

def main():

    parser = argparse.ArgumentParser(description='Program to remove files that match regex in given directory')
    parser.add_argument('-d', '--directory', dest='directory', help='Directory to Clean', required=True)
    parser.add_argument('-k', '--keyword', dest='keyword', help='Keyword search in filename to delete', required=True)
    args = parser.parse_args()

    dirobject = args.directory
    regex = re.compile(args.keyword, re.IGNORECASE)

    for fnobject in listdir(dirobject):
        for match in regex.finditer(fnobject):
            if platform.startswith('win32'):
                file = dirobject + '\\' + fnobject
                remove(file)
            elif platform.startswith('linux'):
                file = dirobject + '/' + fnobject
                remove(file)
            else:
                raise ValueError('Unknown OS')

if __name__ == '__main__':
    main()
