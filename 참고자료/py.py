import pandas as pd
import os
import numpy as np
os.getcwd()

df = pd.read_csv('BrentOilPrices.csv')
df

dataset = list()
month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month_dict = {month_list[m_idx]:m_idx+1 for m_idx in range(len(month_list))}

def bop_data_reader():
    df = pd.read_csv("BrentOilPrices.csv")
    dataset = list()
    month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month_dict = {month_list[m_idx]:m_idx+1 for m_idx in range(len(month_list))}

    for i in range(len(df)):
        price = df.Price[i]
        date = df.Date[i]

        try:
            D, M, Y = date.split(sep='-')
            if int(Y) >= 87:
                M = month_dict[M]
                dataset.append([Y, M, D, price])
        except:
            pass
    dataset = np.array(dataset).astype(np.float)
    return dataset


# 나중에 불러오는 방법 : 이걸 utils.py에 저장해두고,
# from utils import bop_data_reader

dataset = bop_data_reader()

t_year = 90
t_idx = np.where(dataset[:,0] == t_year)
t_data = dataset[t_idx]

t_data