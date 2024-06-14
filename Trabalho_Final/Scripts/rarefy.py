import numpy as np
import pandas as pd
Tabela_original = pd.read_table('c:/Users/jdsie/OneDrive/Python para biocientistas/Tabela_original.tsv')

def Rarefy(Tabela_original):
    '''
    Rarefaction --
    This function processes an OTU table to generate a rarefied one
    Author: Jesus Sierra
    Date: 29/05/2024
    Input: Tabela_original (pandas dataframe)
    Output: Tabela_rarefada (pandas dataframe)
    '''
    
    minreads = Tabela_original[Tabela_original.columns[1:]]
    minreads = minreads.sum(axis=0).min()
    rarefied = Tabela_original.copy()

    for c in Tabela_original.columns[1:]:
        prob = Tabela_original[c] / sum(Tabela_original[c])
        reads = list(np.random.choice(Tabela_original.index, size=minreads, p=prob))
        rarefied[c] = [reads.count(sp) for sp in Tabela_original.index]

    return rarefied
print(Rarefy(Tabela_original))