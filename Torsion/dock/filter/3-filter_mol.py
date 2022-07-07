#!/usr/bin/env python
"""
    python ./filter_mol.py -i aa2ar_out.csv -o aa2ar.csv
"""
import os,sys
import argparse
import gzip

parser = argparse.ArgumentParser(description="Extract molecules without red alert (After analyzing with Torsionchecker).")
parser.add_argument(
    "-i",
    "--input",
    required=True,
    help="input ligand file (.csv)",
)
parser.add_argument(
    "-o",
    "--output",
    required=True,
    help="output ligand file (.csv)",
)

args = parser.parse_args()
infile = args.input
outfile = args.output

f = open(infile, 'r')
out = open(outfile, 'w')
d = {}
d_uniq = {}
for line in f:
    line = line.replace('\t',' ')
    comp_id = line.split()[0]
    comp_energy = line.split()[-1]
    if comp_id not in d.keys():
        li = []
        li.append(comp_energy)
        d[comp_id] = li
    else:
        d[comp_id].append(comp_energy)
for key, value in d.items():
    value = [str(x) for x in value]
    if "R" not in value:
    # if "CHEMBL" in key  or "ZINC" in key and "R" not in value:
        out.write(f'{key},{value}\n')

f.close()
out.close()
