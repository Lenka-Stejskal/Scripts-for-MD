import pysam
import pysamstats

bamfile = pysam.AlignmentFile('picared.bam')
print("P"),
print ("A"),
print ("C"),
print ("G"),
print ("T"),
print ("I"),
print ("D")
for record in pysamstats.stat_variation(bamfile, chrom='gi|11|ref|TL|E1E2J6', fafile="ref_E1E2.fa"):
    print(record['pos']),
    print(record['A']),
    print(record['C']),
    print(record['G']),
    print(record['T']),
    print(record['insertions']),
    print(record['deletions'])
