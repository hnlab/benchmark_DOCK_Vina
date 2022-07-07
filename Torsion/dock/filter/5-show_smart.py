#%%
import pandas as pd
input_file = open("/home/mxu02/dock37-test/test_dude/script/torsion/dock/filter/smiles_type.csv", 'r')
data = pd.read_csv(input_file, sep="\t", header=None, names=["Smart", "Number"])
data.tail(20)

#%%
from rdkit import Chem
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import PandasTools
mol = Chem.MolFromSmarts("[cH1:1][c:2]([cH1])!@[O:3][C:4]")
mol

#%%
# count = 0 
# for i in data.tail(20).Smart:
#     print(i)
#     # count += 1
#     # print(count)
#     mol = Chem.MolFromSmarts("[cH1:1][c:2](cO)!@[O:3][C:4]")
#     # mol = Chem.MolFromSmarts(str(i))
#     mol
