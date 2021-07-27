import pandas as pd 
import numpy as np
import os 
import logging 
logging.basicConfig(filename='logs.log',encoding='utf-8',level=logging.DEBUG)
logging.info('Loading data sets')
store  = pd.read_csv(r'C:\Users\0x030\Desktop\week3\Rossman-sales\data\store.csv')
test  = pd.read_csv(r'C:\Users\0x030\Desktop\week3\Rossman-sales\data\test.csv')
train  = pd.read_csv(r'C:\Users\0x030\Desktop\week3\Rossman-sales\data\train.csv')

logging.info('Loading data sets done')