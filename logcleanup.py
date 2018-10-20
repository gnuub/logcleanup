#!/usr/bin/python

"""logcleanup.py is a script to remove files in a directory that match a case insensitive pattern given through command
 line arguments.
"""

import re
import argparse
from os import listdir, remove
from sys import platform

def main():
    #Create argument parser and expectation for arguments: directory and keyword to search
    parser = argparse.ArgumentParser(description='Program to remove files that match regex in given directory')
    parser.add_argument('-d', '--directory', dest='directory', help='Directory to Clean', required=True)
    parser.add_argument('-k', '--keyword', dest='keyword', help='Keyword search in filename to delete', required=True)
    args = parser.parse_args()

    #Set global variables for directory and pattern from command arguments
    dirobject = args.directory
    regex = re.compile(args.keyword, re.IGNORECASE)

    #Loop through each file in directory to see if filename matches pattern, if so remove it
    for fnobject in listdir(dirobject):
        for match in regex.finditer(fnobject):
            #Check if is a Windows host
            if platform.startswith('win32'):
                file = dirobject + '\\' + fnobject
                remove(file)
            #Check if is a Linux host
            elif platform.startswith('linux'):
                file = dirobject + '/' + fnobject
                remove(file)
            #If OS not Windows or Linux flag an error
            else:
                raise ValueError('Unknown OS')

if __name__ == '__main__':
    main()
