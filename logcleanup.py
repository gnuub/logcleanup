#!/usr/bin/python

"""
Program to remove files that match stem and extension.
"""

from os import listdir


def main():
    logdir = 'C:\\Users\\sookie\\Projects\\Samples\\logs'

    for fsobject in listdir(logdir):
        if 'delete' in fsobject:
            print(fsobject)


if __name__ == '__main__':
    main()
