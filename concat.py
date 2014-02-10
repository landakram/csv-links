import sys
import csv

first = sys.argv[1]
rest = sys.argv[2:]

with open(first, 'rb') as f:
    print f.read()
    for a_file in rest:
        with open(a_file, 'rb') as fi:
            fi.readline() # throw away header
            print fi.read()

