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
