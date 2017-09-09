# Copyright (c) 2017 Lenka Stejskal

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


# Create a table showing tleap-style residue numbers alongside the corresponding PDB residue/chain

__author__ = 'Lenka Stejskal'



import fileinput
import sys
import argparse

def main(argv):
    parser = argparse.ArgumentParser(description='Remove H records from a PDB')
    parser.add_argument('infile', help='input file (PDB format)')
    parser.add_argument('outfile', help='output file (PDB format)')
    parser.add_argument('chain', help='chain')
    args = parser.parse_args()

    if len(args.chain) > 1:
        print 'Error: chain must be a single letter'
        quit()

    with open(args.infile, "r") as f, open(args.outfile, "w") as of:
        for line in f:
            if len(line) > 26 and line[:6] == 'ATOM  ':
                chain = line[21]
                of.write(line.replace(line[21],args.chain))

if __name__ == "__main__":
    main(sys.argv)
