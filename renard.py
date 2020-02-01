#!/usr/bin/python

import argparse
from renard_tools import os, sort, rename

# TODO: rename files in subdirectories
parser = argparse.ArgumentParser(description = 'Rename files in the directory, using naming conventions')
parser.add_argument('name', help = 'name convention')
parser.add_argument('-d', '--directory', default=os.getcwd(), help = 'directory, which contains files')
parser.add_argument('-n', '--number', type = int, help = 'number of files to rename')
parser.add_argument('-i', '--include', action = 'store_true', default = False, help = 'rename subfolders as well')
parser.add_argument('-s', '--sort', choices=['d', 'n', 's', 'rd', 'rn', 'rs'], default = 'n',
                    help = 'sorting order [d - date, n - name, s - size, r[letter] - reverse order]')

args = parser.parse_args()
files = sort(args)
rename(args, files)
