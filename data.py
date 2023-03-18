import pandas as pd

def get_data(path="Ref_Heart_Wave_1.csv", start = 0 , end = 2000):

    data = pd.read_csv(path)
    return (data.iloc[start:end,0]).to_list()
# print(get_data())