import pandas as pd 
import numpy as np  
# data frame 1
d1 = pd.read_csv('dataset_1.csv')
df1 = pd.DataFrame(d1)
# data frame 2
d2 = pd.read_csv('dataset_2.csv')
df2 = pd.DataFrame(d2)
#print(d1)
#print(d2)
df = pd.merge(df1,df2, on='NAME', how='inner')
print(df)
df_1 = pd.DataFrame(df['STANCE'])
