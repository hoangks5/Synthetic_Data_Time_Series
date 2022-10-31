import random
import pandas as pd
import os
data_source = 'website_classification.csv'


with open(data_source,'r',encoding='utf-8') as f:
    st = f.read()
s = st.splitlines()
for i in s:
    t = i.split(',')
    print(t[4])
    
            