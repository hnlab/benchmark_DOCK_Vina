#%%
# Analysis of correlation between -logKd(Ki) and MW, statistics from PDBbind v2003.
import pandas as pd
input_file = pd.read_csv('merge_pka_MW.csv', sep = ' ', header=None, names=["PDB code", "resolution", "release year", "logKd", "reference", "-", "MW"])
input_file.head()

#%%
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import spearmanr, pearsonr
plt.figure(figsize=(6, 6), facecolor='w', edgecolor='k')
# plt.figure(figsize=(8,8))
sns.set(font_scale=1.2)
sns.set_style("white")

x=input_file.MW
y=input_file.logKd
xy = np.vstack([x,y])
z = stats.gaussian_kde(xy)(xy)
Rp, p_value=pearsonr(x,y)
plt.scatter(x, y, c=z, s=40)

plt.xlabel("MW", size=16)
# plt.ylabel("-log${K_d}$${(K_i)}$", size=16)
plt.ylabel("-log${K_d}$ or -log${K_i}$", size=16)
plt.title("Rp={:.4f}   p_value={:.3}".format(Rp, p_value))
plt.savefig("/home/mxu02/test/PDBbind_MW.png", dpi=300)
print(Rp,p_value)
#%%
