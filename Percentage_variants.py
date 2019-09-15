import sys
import argparse
import operator

def main (argv):
    parser = argparse.ArgumentParser(description='Get the variants that are present at least 5% of the time ')
    parser.add_argument('infile', help='file to process')
    parser.add_argument('outfile', help='file to produce')
    args = parser.parse_args()
    done =[]

    with open(args.infile, "r") as f, open(args.outfile, "w") as of:
        file_in = f.readlines()
        for line in file_in:
                temp = line.split()
                if temp[0] != "P":
                    A = temp[1]
                    C = temp[2]
                    G = temp[3]
                    T = temp[4]
                    I = temp[5]
                    D = temp[6]
                    total = int(A) + int(C) + int(G) + int(T) + int(I) + int(D)
                    if int(total) >= 1000:
                        Onepercent = float(total) / 100
                        FivePercent = float(Onepercent) * 5
                        if int(A) >= float(FivePercent) and int(C) >= float(FivePercent):
                            of.write(line)
                        elif int(A) >= float(FivePercent) and int(G) >= float(FivePercent):
                            of.write(line)
                        elif int(A) >= float(FivePercent) and int(T) >= float(FivePercent):
                            of.write(line)
                        elif int(C) >= float(FivePercent) and int(G) >= float(FivePercent):
                            of.write(line)
                        elif int(C) >= float(FivePercent) and int(T) >= float(FivePercent):
                            of.write(line)
                        elif int(G) >= float(FivePercent) and int(T) >= float(FivePercent):
                            of.write(line)

if __name__ == "__main__":
    main(sys.argv)
