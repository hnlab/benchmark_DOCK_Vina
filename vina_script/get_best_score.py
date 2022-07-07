#!/usr/bin/python
with open('vina.txt','r') as f:
    d = {}
    for line in f:
        line = line.replace('_',' ')
        comp_id = line.split()[0]
        comp_energy = line.split()[4]
        if comp_id not in d.keys():
            li = []
            li.append(comp_energy)
            d[comp_id] = li
        else:
            d[comp_id].append(comp_energy)
with open('vina_out.txt','w') as outfile:
    for key, value in d.items():
        value = [float(x) for x in value]
        result = min(value)
        outfile.writelines(str(key) + " " + str(result) + "\n")
f.close()
outfile.close()
