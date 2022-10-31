import random
import pandas as pd
import os
folder = pd.read_csv(data_source,index_col=False)

with open(data_source,'r',encoding='utf-8') as f:
    st = f.read()
    
            