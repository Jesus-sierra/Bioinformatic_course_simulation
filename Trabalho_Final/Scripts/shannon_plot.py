import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tabela_original = pd.read_table('c:/Users/jdsie/OneDrive/Python para biocientistas/Tabela_original.tsv')
tabela_rarefada = pd.read_table('c:/Users/jdsie/OneDrive/Python para biocientistas/Tabela_rarefada.tsv')
tabela_normalizada = pd.read_table('c:/Users/jdsie/OneDrive/Python para biocientistas/Tabela_normalizada.tsv')

def shannon(tabela):
    copied_table = tabela[tabela.columns[1:]].copy()
    copied_table /= copied_table.sum(axis=0)
    copied_table *= np.log(copied_table)
    copied_table = -1 * copied_table.sum(axis=0)
    return copied_table


shannon_total = pd.concat([shannon(tabela_rarefada),
                           shannon(tabela_normalizada)],
                           axis=1)

shannon_total.columns = ['Rarefied', 'Normalized']
print(shannon_total)
shannon_total.to_csv('tabela_shannon.tsv', sep='\t', header=True, index=True)

sns.scatterplot(data=shannon_total)
plt.xlabel('Samples')
plt.ylabel('Shannon index')

plt.savefig('Shannon.png', dpi=1200)