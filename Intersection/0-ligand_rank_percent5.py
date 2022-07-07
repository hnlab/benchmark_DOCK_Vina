#!/usr/bin/python

from __future__ import division
import re
import sys
from pathlib import Path
import pandas as pd
from collections import defaultdict

base_dir = Path("/home/mxu02/dock37-test/test_dude")

ligands_smi_dict = {}
target = sys.argv[1] # please input target name, like AA2AR
total_input = base_dir / target / "dock37/dock/mol.name"
ligands_smi = base_dir / target / "dock37/ligand/actives_final.ism"

with open(ligands_smi, 'r') as f:
    for line in f:
        smiles = line.split()[0]
        ligand_name = line.split()[2]
        ligands_smi_dict[ligand_name] = smiles
    # print(ligands_smi_dict)

def sum_count(file_name):
    return sum(1 for _ in open(file_name))

dock_total = []
dock_rank = 0
# dock_energies_dict = defaultdict(list)
outfile = open('top5_outfile.csv','a')
total_line = sum_count(total_input)
dock_input = base_dir / target / "dock37/dock/extract_all.sort.uniq.txt"
with open(dock_input, 'r') as f:
    for line in f:
        name = line.split()[2]
        energy = line.split()[-1]
        dock_total.append(name)
        if "CHEMBL" in name and len(dock_total) <= 0.05 * total_line + 1:
            dock_rank = len(dock_total)
            ligand_smi = ligands_smi_dict[name]
            outfile.write("{},dock,{},{},{:.2f},{}\n".format(target,name,ligand_smi,float(energy),dock_rank))

vina_total = []
vina_rank = 0
vina_input = base_dir / target / "vina/output/extract_all.sort.uniq.txt"
with open(vina_input, 'r') as f2:
    for line in f2:
        name = line.split()[2]
        energy = line.split()[-1]
        vina_total.append(name)
        if "CHEMBL" in name and len(vina_total) <= 0.05 * total_line + 1:
            vina_rank = len(vina_total)
            ligand_smi = ligands_smi_dict[name]
            outfile.write("{},vina,{},{},{:.2f},{}\n".format(target,name,ligand_smi,float(energy),vina_rank))
    # outfile.write("\n")
outfile.close()
