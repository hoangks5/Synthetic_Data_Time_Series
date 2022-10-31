import random
import pandas as pd
import os
data_source = 'website_classification.csv'

frame_new = ['Travel',
 'Social Networking and Messaging',
 'News',
 'Streaming Services']
a = []
with open(data_source,'r',encoding='utf-8') as f:
    st = f.read()
s = st.splitlines()
for i in s:
    t = i.split(',')
    if t[3] in frame_new:
        a.append(i)
        
strings = '\n'.join(a)
w = open('./data/data(1-4).csv','w',encoding='utf-8')
w.write(strings)
w.close()
            