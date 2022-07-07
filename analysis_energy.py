# %%
from pathlib import Path
from numpy.lib.function_base import disp

base_dir = Path("/home/mxu02/dock37-test/test_dude")
# %%
target = "aa2ar"
# %%
ligands_smi = base_dir / target / "dock37/ligand/actives_final.ism"
decoys_smi = base_dir / target / "dock37/ligand/decoys_final.ism"
# %%
import pandas as pd

ligands = pd.read_csv(ligands_smi, sep=" ", header=None, names=["smiles", "number", "name"])

# %%
decoys = pd.read_csv(decoys_smi, sep=" ", header=None, names=["smiles", "name"])

# %%
from IPython.display import display

decoys["class"] = "decoy"
ligands["class"] = "active"
data = pd.concat([decoys, ligands], ignore_index=True)
# display(data.head())
# display(data.tail())

#%%
from rdkit.Chem import PandasTools

PandasTools.AddMoleculeColumnToFrame(data, smilesCol="smiles", molCol="mol")

# %%
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


# %%
prop_names = ["MW", "logP", "rotB", "HBD", "HBA", "Q"]
props = []
for m in data.mol:
    props.append(PROP(m))
props_T = list(zip(*props))
for p_name, p_values in zip(prop_names, props_T):
    data[p_name] = p_values
data.head()
# %%
import seaborn as sns

# required seaborn 0.11
sns.histplot(data, x="MW", hue="class")
# %%
sns.histplot(data, x="MW", hue="class", stat="density", common_norm=False)
# %%
from matplotlib import pyplot as plt

fig, axes = plt.subplots(nrows=6, figsize=(12, 24))
for name, ax in zip(prop_names, axes.flat):
    sns.histplot(data, x=name, hue="class", stat="density", common_norm=False, ax=ax)

# %%
# vina_result = "/home/mxu02/dock37-test/test_dude/andr/vina/extract_all.sort.uniq.txt"
vina_result = base_dir / target / "vina/output/extract_all.sort.uniq.txt"
# print(vina_result.read_text()[:300])
# %%
import re

vina_energies_dict = {}
with open(vina_result) as f:
    for line in f:
        fields = line.split()
        name = fields[2]
        energy = fields[-1]
        vina_energies_dict[name] = float(energy)
# %%
vina_energies = [vina_energies_dict.get(name, None) for name in data.name]
data["vina"] = vina_energies
data.head()
# %%
sns.histplot(data, x="vina", hue="class", stat="density", common_norm=False, kde=True)
# fig=plt.gcf()
# fig.savefig("/home/mxu02/dock37-test/test_dude/aa2ar/aa2ar_vina_energy.png", dpi=125, bbox_inches='tight')
# %%
outlier_mask = data.vina > 0
vina_outliers = data[outlier_mask]
data = data[~outlier_mask] # including nan
print(f"remove {len(vina_outliers)} vina outliers")
display(vina_outliers)
display(vina_outliers[["name", "mol"]])
# %%
sns.histplot(data, x="vina", hue="class", stat="density", common_norm=False, kde=True)

# %%
fig=sns.pairplot(data, x_vars=["vina"] + prop_names, y_vars=["vina"], hue="class")
fig=plt.gcf()
fig.savefig("/home/mxu02/dock37-test/test_dude/aa2ar/aa2ar_vina_scatter.png", dpi=125, bbox_inches='tight')

# %%
# dock_result = "/home/mxu02/dock37-test/test_dude/andr/dock37/dock/extract_all.sort.uniq.txt"
dock_result = base_dir / target / "dock37/extract_all.sort.uniq.txt"
# print(dock_result.read_text()[:300])
# %%
dock_energies_dict = {}
with open(dock_result) as f:
    for line in f:
        fields = line.split()
        name = fields[2]
        energy = fields[-1]
        dock_energies_dict[name] = float(energy)
dock_energies = [dock_energies_dict.get(name, None) for name in data.name]
data["dock"] = dock_energies
# data.head()

# %%
sns.histplot(data, x="dock", hue="class", stat="density", common_norm=False, kde=True)
# fig=plt.gcf()
# fig.savefig("/home/mxu02/dock37-test/test_dude/aa2ar/aa2ar_dock_energy.png", dpi=125, bbox_inches='tight')
# %%
fig=sns.pairplot(data, x_vars=["dock"] + prop_names, y_vars=["dock"], hue="class")
fig=plt.gcf()
fig.savefig("/home/mxu02/dock37-test/test_dude/aa2ar/aa2ar_dock_scatter.png", dpi=125, bbox_inches='tight')

# %%
fig= sns.scatterplot(data=data, x="vina", y="dock", hue="class")
fig=plt.gcf()
fig.savefig("/home/mxu02/dock37-test/test_dude/aa2ar/aa2ar_dock_vina.png", dpi=125, bbox_inches='tight')
# %%
