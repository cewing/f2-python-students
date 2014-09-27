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

    inlines = io.open(infilename).readlines()
    outlines = map(string.strip, inlines)

    # add a newline back in:
    outfile = io.open(outfilename, 'w')
    for line in outlines:
        outfile.write(line+"\n")




