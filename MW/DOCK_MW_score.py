#%%
# script to plot molecules according to their vina score and MW.
ligands_smi = "/home/mxu02/dock37-test/test_dude/script/MW_analysis/all_ligand.ism"
decoys_smi = "/home/mxu02/dock37-test/test_dude/script/MW_analysis/all_decoy.ism"

#%%
import pandas as pd

# ligands = pd.read_csv(ligands_smi, sep=" ", header=None, names=["smiles", "number", "name"])
ligands = pd.read_csv(ligands_smi, sep=" ", header=None, names=["smiles", "name"])
ligands.head()
decoys = pd.read_csv(decoys_smi, sep=" ", header=None, names=["smiles", "name"])
decoys.head()

#%%
from IPython.display import display

decoys["class"] = "decoy"
ligands["class"] = "active"
data = pd.concat([decoys, ligands], ignore_index=True, sort=False)

#%%
from rdkit.Chem import PandasTools

PandasTools.AddMoleculeColumnToFrame(data, smilesCol="smiles", molCol="mol")
# data.head()

#%%
from rdkit import Chem

def PROP(mol):
    from rdkit.Chem import Descriptors

    mw = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)
    rotb = Descriptors.NumRotatableBonds(mol)
    hbd = Descriptors.NumHDonors(mol)
    hba = Descriptors.NumHAcceptors(mol)
    q = Chem.GetFormalCharge(mol)
    return tuple([mw, logp, rotb, hbd, hba, q])

#%%
prop_names = ["MW", "logP", "rotB", "HBD", "HBA", "Q"]
props = []
for m in data.mol:
    props.append(PROP(m))
props_T = list(zip(*props))
for p_name, p_values in zip(prop_names, props_T):
    data[p_name] = p_values
data.head()

#%%
# import seaborn as sns
# # required seaborn 0.11
# sns.histplot(data, x="MW", hue="class")

#%%
# sns.histplot(data, x="MW", hue="class", stat="density", common_norm=False)

#%%
from matplotlib import pyplot as plt
import seaborn as sns

# fig, axes = plt.subplots(nrows=6, figsize=(12, 24))
# for name, ax in zip(prop_names, axes.flat):
#     sns.histplot(data, x=name, hue="class", stat="density", common_norm=False, ax=ax)
#     fig=plt.gcf()
#     fig.savefig("/home/mxu02/dock37-test/test_dude/script/MW_analysis/all_property.png", dpi=125, bbox_inches='tight')

#%%
import pandas as pd
vina_result = "/home/mxu02/dock37-test/test_dude/script/MW_analysis/dock/all_dock_success.csv"
# vina_result = "/home/mxu02/dock37-test/test_dude/script/MW_analysis/dock/test.csv"
#%%
import re

vina_energies_dict = {}
with open(vina_result) as f:
    for line in f:
        fields = line.split()
        name = fields[2]
        energy = fields[-1]
        vina_energies_dict[name] = float(energy)

#%%
vina_energies = [vina_energies_dict.get(name, None) for name in data.name]
data["vina"] = vina_energies
data.head()

#%%
# sns.histplot(data, x="vina", hue="class", stat="density", common_norm=False, kde=True)

outlier_mask = data.vina > 10
vina_outliers = data[outlier_mask]
data = data[~outlier_mask] # including nan
print(f"remove {len(vina_outliers)} vina outliers")
display(vina_outliers)
display(vina_outliers[["name", "mol"]])

#%%
import pandas as pd
import numpy as np
np.isnan(data["vina"]).any()
np.isnan(data["MW"]).any()
np.isinf(data["vina"])
score=data.dropna()
score.head()
# score = [not pd.isnull(number) for number in data["vina"]]
# print(len(score))
#%%
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import spearmanr, pearsonr
plt.figure(figsize=(8, 8), facecolor='w', edgecolor='k')
sns.set(font_scale=1.2)
sns.set_style("white")

x=score.MW
# y=data.vina
y=score.vina
xy = np.vstack([x,y])
z = stats.gaussian_kde(xy)(xy)
Rp, p_value=pearsonr(x,y)
plt.scatter(x, y, c=z, s=20)
plt.xlabel("MW", size=15)
plt.ylabel("DOCK 3.7", size=15)
plt.title("Rp={:.4f}   p_value={:.3}".format(Rp, p_value))
# plt.show()
plt.savefig("/home/mxu02/dock37-test/test_dude/script/MW_analysis/dock/dock_score.png", dpi=300)
print(Rp,p_value)

#%%
