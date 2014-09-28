#!/usr/bin/env python

"""
clean_files script:

removes all the whitespace before and after each line in a text file

CAUTION: do not run this on a Python code file!
"""

import sys
import io
import string # for the strip() function


help_msg = """clean_files infilename [outfilename]

Strips the whitespace off the front and back of each line in infilename.

If you provide a second filename, the cleaned data will be written to
that file. Otherwise the original file will be overridden.
"""


def clean_file(infilename, outfilename):
    """ solution using map """

    inlines = io.open(infilename).readlines()

    outlines = map(string.strip, inlines)

    # add a newline back in when writing:
    outfile = io.open(outfilename, 'w')
    for line in outlines:
        outfile.write(line+"\n")


def clean_file2(infilename, outfilename):
    """ solution using list comprehension """

    inlines = io.open(infilename).readlines()

    outlines = [line.strip()+"\n" for line in inlines]

    io.open(outfilename, 'w').writelines(outlines)


def clean_file3(infilename, outfilename):
    """ solution as a one-liner """

    io.open(outfilename, 'w').writelines( [line.strip()+"\n" for line in io.open(infilename).readlines()] )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print help_msg
        sys.exit(1)
    else:
        infilename = sys.argv[1]
        try:
            outfilename = sys.argv[2]
        except IndexError:
            outfilename = infilename

    clean_file(infilename, outfilename)
    # clean_file2(infilename, outfilename)
    # clean_file3(infilename, outfilename)




