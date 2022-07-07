#%%
#!/usr/bin/env python
# get dihedraldeg of every rotateable bond with rdkit.
# Single molecule

from rdkit import Chem
from rdkit.Chem import AllChem

molH = Chem.rdmolfiles.MolFromMol2File("test.mol2")

confs = molH.GetConformers()
diheds = [Chem.rdMolTransforms.GetDihedralDeg(conf, 28, 19, 16, 18) for conf in confs]
print(diheds)

#%%
#!/usr/bin/env python
# get dihedraldeg of every rotateable bond with rdkit.
# Multiple molecules。
# 还有bug，需要进一步定义 torsion 哪些分子等信息！ 环内分子二面角不用计算！

import os
from rdkit import Chem
from rdkit.Chem import AllChem


def Mol2MolSupplier (file=None,sanitize=True):
    mols=[]
    with open(file, 'r') as f:
        line =f.readline()
        while not f.tell() == os.fstat(f.fileno()).st_size:
            if line.startswith("@<TRIPOS>MOLECULE"):
                mol = []
                mol.append(line)
                line = f.readline()
                while not line.startswith("@<TRIPOS>MOLECULE"):
                    mol.append(line)
                    line = f.readline()
                    if f.tell() == os.fstat(f.fileno()).st_size:
                        mol.append(line)
                        break
                mol[-1] = mol[-1].rstrip() # removes blank line at file end
                block = ",".join(mol).replace(',','')
                m=Chem.MolFromMol2Block(block,sanitize=sanitize)
            mols.append(m)
    return(mols)

filePath = open('/home/mxu02/dock37-test/test_dude/script/torsion/test_mul.mol2','r')
database=Mol2MolSupplier(filePath,sanitize=True)
for molH in database:
    if molH:
        confs = molH.GetConformers()
        diheds = [Chem.rdMolTransforms.GetDihedralDeg(conf, 28, 19, 16, 18) for conf in confs]
        print(diheds)
filePath.close()

#%%
import matplotlib.pyplot as plt
plt.style.use('ggplot')

fig,ax = plt.subplots()
n,bins,patches = ax.hist(diheds,bins=36)
ax.set_xlabel('Dihedral Angle')
ax.set_ylabel('Counts')

#%%
