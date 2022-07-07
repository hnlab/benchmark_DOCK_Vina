#!/usr/bin/python

from __future__ import division
import sys
from pathlib import Path

base_dir = Path("/home/mxu02/dock37-test/test_dude")
target = sys.argv[1]
dock_input = base_dir / target / "dock37/dock/extract_all.sort.uniq.txt"
vina_input =  base_dir / target / "vina/output/extract_all.sort.uniq.txt"
total_input =  base_dir / target / "dock37/dock/mol.name"
total_ligand =  base_dir / target / "dock37/dock/ligand.name"

def sum_count(file_name):
    return sum(1 for _ in open(file_name))

total = []
dock_list = []
total_line = sum_count(total_input)
total_lig = sum_count(total_ligand)
print(total_line,total_lig)

with open(dock_input, 'r') as f:
    for line in f:
        name = line.split()[2]
        total.append(name)
        if "CHEMBL" in name and len(total) <= 0.01 * total_line:
            dock_list.append(name)
    d_num = len(dock_list)
    EF1_dock = (d_num/int(0.01 * total_line))/(total_lig/total_line)

vina_total = []
vina_list = []
with open(vina_input, 'r') as f2:
    for line in f2:
        name = line.split()[2]
        vina_total.append(name)
        if "CHEMBL" in name and len(vina_total) <= 0.01 * total_line:
            vina_list.append(name)

    v_num = len(vina_list)
    EF1_vina = (v_num/int(0.01 * total_line))/(total_lig/total_line)

outfile = open("EF1.csv", 'a')
outfile.write(f'{target},{round(EF1_dock,2)},{round(EF1_vina,2)}\n')
outfile.close()
