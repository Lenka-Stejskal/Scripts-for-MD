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



import sys
import argparse
import operator

def main (argv):
    parser = argparse.ArgumentParser(description='Sort out the model by the total energy score')
    parser.add_argument('infile', help='file to process')
    parser.add_argument('outfile', help='file to produce')
    args = parser.parse_args()
    values = {}
    energy =[]
    name = []

    with open(args.infile, "r") as f:
        file_in = f.readlines()[2:]
        for line in file_in:
            temp = line.split()
            if temp[0] == "SCORE:":
                energy_values = temp[1]
                name_values = temp[32]
                energy.append(energy_values)
                name.append(name_values)

    with open(args.outfile,"w+") as of:
        values = dict(zip(name, energy))
        results = sorted(values.items(), key=lambda kv: float(kv[1]), reverse=False)
        for k,v in results:
            of.write(k+'\n')


if __name__ == "__main__":
    main(sys.argv)
