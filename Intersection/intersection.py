#!/usr/bin/python

from __future__ import division
import sys
from pathlib import Path

base_dir = Path("/home/mxu02/dock37-test/test_dude")
target = sys.argv[1]
dock_input = base_dir / target / "dock37/dock/extract_all.sort.uniq.txt"
vina_input =  base_dir / target / "vina/output/extract_all.sort.uniq.txt"
total_input =  base_dir / target / "dock37/dock/mol.name"

def sum_count(file_name):
    return sum(1 for _ in open(file_name))

total = []
dock_list = []
total_line = sum_count(total_input)
print(total_line)
outfile = open("intersection.csv","a")
with open(dock_input, 'r') as f:
    for line in f:
        name = line.split()[2]
        total.append(name)
        if "CHEMBL" in name and len(total) <= 0.05 * total_line + 1:
            dock_list.append(name)

vina_total = []
vina_list = []
with open(vina_input, 'r') as f2:
    for line in f2:
        name = line.split()[2]
        vina_total.append(name)
        if "CHEMBL" in name and len(vina_total) <= 0.05 * total_line + 1:
            vina_list.append(name)

mol_number = dock_number = vina_number = 0
for mol in dock_list:
    if mol in vina_list:
        mol_number += 1
    else:
        dock_number += 1
vina_number = len(vina_list) - mol_number
outfile.write("{} intersection:{} dock:{} vina:{}\n".format(target, mol_number, dock_number, vina_number))
# outfile.write("{} intersection:{:.4f} dock:{:.4f} vina:{:.4f}\n".format(target, float(mol_number/(0.05 * total_line)), float(dock_number/(0.05 * total_line)), float(vina_number/(0.05 * total_line))))
outfile.close()
