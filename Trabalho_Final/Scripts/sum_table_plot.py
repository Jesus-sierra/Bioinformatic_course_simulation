import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#import tables
tabela_original = pd.read_table('c:/Users/jdsie/OneDrive/Python para biocientistas/Tabela_original.tsv')
tabela_rarefada = pd.read_table('c:/Users/jdsie/OneDrive/Python para biocientistas/Tabela_rarefada.tsv')
tabela_normalizada = pd.read_table('c:/Users/jdsie/OneDrive/Python para biocientistas/Tabela_normalizada.tsv')

#generates the mean per group with standard deviation
original_sum = tabela_original.drop('OTU', axis=1).sum(axis=0)
rarefied_sum = tabela_rarefada.drop('OTU', axis=1).sum(axis=0)
normalized_sum = tabela_normalizada.drop('OTU', axis=1).sum(axis=0)

# Create the mean table
summed_data = pd.concat([original_sum,
                         rarefied_sum,
                         normalized_sum],
                        axis=1)

summed_data.columns = ['Original', 'Rarefeita', 'Normalizada']

print(summed_data)

summed_data.to_csv('tabela_somas.tsv', sep='\t', header=True, index=True)

sns.boxplot(data=summed_data)

plt.savefig('Sum_treatments.png', dpi=1200)