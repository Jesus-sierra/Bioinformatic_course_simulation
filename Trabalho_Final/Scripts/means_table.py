import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import tables
tabela_original = pd.read_table('c:/Users/jdsie/OneDrive/Python para biocientistas/Tabela_original.tsv')
tabela_rarefada = pd.read_table('c:/Users/jdsie/OneDrive/Python para biocientistas/Tabela_rarefada.tsv')
tabela_normalizada = pd.read_table('c:/Users/jdsie/OneDrive/Python para biocientistas/Tabela_normalizada.tsv')

#remove the index to work only with numbers
original_no_index = tabela_original.iloc[:, 1:].values
rarefied_no_index = tabela_rarefada.iloc[:, 1:].values
normalized_no_index = tabela_normalizada.iloc[:, 1:].values

#generates the mean per group with standard deviation
original_mean_std = [original_no_index.sum(axis=0).mean(), original_no_index.sum(axis=0).std()]
rarefied_mean_std = [rarefied_no_index.sum(axis=0).mean(), rarefied_no_index.sum(axis=0).std()]
normalized_mean_std = [normalized_no_index.sum(axis=0).mean(), normalized_no_index.sum(axis=0).std()]

# Create the mean table
mean_table = pd.DataFrame([original_mean_std, rarefied_mean_std, normalized_mean_std],
                          columns=['Mean', 'STD'],
                          index=['Original', 'Rarefeita', 'Normalizada'])

print(mean_table)

mean_table.to_csv('tabela_medias.tsv', sep='\t', header=True, index=True)