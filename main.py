import random
import pandas as pd
import os
data_source = 'website_classification.csv'

frame_new = ['Travel',
 'Social Networking and Messaging',
 'News',
 'Streaming Services']
with open(data_source,'r',encoding='utf-8') as f:
    st = f.read()
s = st.splitlines()
for i in s:
    t = i.split(',')
    if t[3] in frame_new:
        print(i)
    
            