import pandas as pd

def TSS(Tabela_original):
    '''
    Normalization --
    This function processes an OTU table to generate a normalized one
    Author: Jesus Sierra
    Date: 29/05/2024
    Input: Tabela_original (pandas dataframe)
    Output: Tabela_normalizada (pandas dataframe)
    '''
    tss_table = Tabela_original.copy().set_index('OTU')
    tss_table *= tss_table.sum(axis=0).max()
    tss_table /= Tabela_original.sum(axis=0)
    tss_table = tss_table.astype('int')
    return tss_table.reset_index()

Tabela_original = pd.read_table('c:/Users/jdsie/OneDrive/Python para biocientistas/Tabela_original.tsv')
print(TSS(Tabela_original))