#%%
from pathlib import Path
from numpy.lib.function_base import disp

base_dir = Path("/home/mxu02/dock37-test/test_dude/dude/all")
# list(base_dir.glob("*"))

#%%
target = "kpcb"
# list(base_dir.glob(f"{target}/*"))

#%%
ligands_smi = base_dir / target / "actives_final.ism"
decoys_smi = base_dir / target / "decoys_final.ism"
# print(ligands_smi.read_text()[:300])

#%%
import pandas as pd

ligands = pd.read_csv(ligands_smi, sep=" ", header=None, names=["smiles", "number", "name"])
ligands.head()
decoys = pd.read_csv(decoys_smi, sep=" ", header=None, names=["smiles", "name"])
decoys.head()

#%%
from IPython.display import display

decoys["class"] = "decoy"
ligands["class"] = "active"
data = pd.concat([decoys, ligands], ignore_index=True)
# display(data.head())
# display(data.tail())

#%%
from rdkit.Chem import PandasTools

PandasTools.AddMoleculeColumnToFrame(data, smilesCol="smiles", molCol="mol")
# data.head()

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
# data.head()

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
    fig=plt.gcf()
    fig.savefig("/home/mxu02/dock37-test/test_dude/kpcb/kpcb_property.png", dpi=125, bbox_inches='tight')

#%%
