#!/usr/bin/python
import math
def coord(x):
    x_co = max(x) - min(x) + 15
    return math.ceil(x_co)

if __name__ == '__main__':
    x_coord = []
    y_coord = []
    z_coord = []
    file_name = open('xtal-lig.pdb', 'r')
    lines = file_name.readlines()
    for line in lines:
        if 'ATOM' in line.split() or 'HETATM' in line.split():
            x_coord.append(float(line.split()[6]))
            y_coord.append(float(line.split()[7]))
            z_coord.append(float(line.split()[8]))
size_x = coord(x_coord)
size_y = coord(y_coord)
size_z = coord(z_coord)
with open ('conf.txt', 'a') as f:
    f.write('\n' + 'size_x = '+ str(size_x) + '\n' +'size_y = '+ str(size_y) + '\n' + 'size_z = ' + str(size_z) + '\n' + '\n' + 'exhaustiveness = 8')
file_name.close()
