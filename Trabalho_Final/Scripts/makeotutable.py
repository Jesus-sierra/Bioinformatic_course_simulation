import numpy as np
import pandas as pd

def maketable():
    array = np.array([np.random.randint(4000,
                                        size=(26)) for i in range(100)])
    df = pd.DataFrame(array,
                      columns=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                               'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                               'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                               'y', 'z'],
                      index=[f'OTU_{i+1}' for i in range(0, 100)])
    zeros = np.random.choice(range(40, 75),
                             size=26)
    for z, column in zip(zeros,
                         df.columns):
        indexes = df.sample(z).index
        for idx in indexes:
            df.loc[idx, column] = 0
    df = df.reset_index()
    df = df.rename({'index': 'OTU'},
                   axis=1)
    return df

otu_table = maketable()
print(otu_table)