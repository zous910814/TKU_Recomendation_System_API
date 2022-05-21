import pandas as pd

df = pd.read_csv("./tkudata/學生資料/1-3學生各科成績(期中).csv")

print(df[df['req_ele_type']=="C"]['ch_cos_name'].nunique())