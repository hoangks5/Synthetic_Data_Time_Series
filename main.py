import random
import pandas as pd
import os
data_source = 'AAPL Historical Data.csv'
os.mkdir(data_source.split('.')[0])
original_df = pd.read_csv(data_source)
for i in range(30):
    