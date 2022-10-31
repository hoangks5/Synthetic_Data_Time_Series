import random
import pandas as pd
import os
import json
data_source = 'website_classification.csv'

w = open('./data/data(1-4).csv','r',encoding='utf-8').read().splitlines()
for i in w[0:100]:
    a = i.split(',')[1]
    json_new = """{"website": "<iframe src='"""+a+"""'width='100%' height='600px'/>"}"""
    
    with open("./data/data1-4/data("+str(random.randint(1,99999))+").json", "w") as outfile:
        outfile.write(json_new)