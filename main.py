import random
import pandas as pd
import os

### Create file csv data from sample
data_source = 'AAPL Historical Data.csv'
folder = data_source.split('.')[0]
os.mkdir(folder)
data_original = pd.read_csv(data_source)
for i in range(20):
    index_random = random.randint(0,len(data_original['Date'])-60)
    data = data_original['Price']
    for index in range(len(data)):
        data[index] += data[index]*random.randint(-30,30)/100
    data_original['Price'] = data
    data_original.to_csv('./train.csv',index=False)
    
    