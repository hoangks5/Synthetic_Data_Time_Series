import random
import pandas as pd
import os
data_source = 'website_classification.csv'

w = open('./data/data(1-4).csv','r',encoding='utf-8').read().splitlines()
for i in w:
    a = i.split(',')
    print(a[1])
    json_new = {
    "website": "<iframe src='{a}' width='100%' height='600px'/>"
}