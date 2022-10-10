import random
import pandas as pd
import os

### Create file csv data from sample
data_source = 'AAPL Historical Data.csv'
os.mkdir(data_source.split('.')[0])
data_original = pd.read_csv(data_source)
for i in range(30):
    data = data_original['Price']
    for index in range(len(data)):
        data[index] += data[index]*random.randint(-30,30)/100
    data_original['Price'] = data
    data_original.to_csv('./train.csv',index=False)
    