import random
import pandas as pd
import os

### Create file csv data from sample
data_source = 'Sliver.csv'
folder = data_source.split('.')[0]
try:
    os.mkdir(folder)
except:
    pass
data_original = pd.read_csv(data_source)
for i in range(20): 
    index_random = random.randint(0,len(data_original['Date'])-60)
    data_original_new = data_original[index_random:index_random+60]
    data_original_new.to_csv(folder+'/'+folder+'('+str(i+1)+').csv',index=False)
    
    data_original_new = pd.read_csv(folder+'/'+folder+'('+str(i+1)+').csv')
    data = data_original_new['Price']
    for index in range(len(data)):
        data[index] += data[index]*random.randint(-30,30)/100
    data_original_new['Price'] = data
    data_original_new.to_csv(folder+'/'+folder+'_fake('+str(i+1)+').csv',index=False)
    
            