#!/usr/bin/python
out_file = open("out_lig.csv",'w')
with open("extract_all.sort.uniq.txt",'r') as f:
    for line in f:
        if "CHEMBL" in line:
            lig_name = line.split()[2]
            lig_energy = float(line.split()[-1])
            out_file.write("{},{:.3f}\n".format(lig_name, lig_energy))
out_file.close()
