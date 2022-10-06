import gretel
import pandas as pd

data_source = 'https://gretel-public-website.s3.amazonaws.com/datasets/credit-timeseries-dataset.csv'
original_df = pd.read_csv(data_source)
original_df