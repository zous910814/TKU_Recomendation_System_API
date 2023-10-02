import pandas as pd

df = pd.read_csv("../tkudata/課程資料/2-1開課資料.csv")
# df.to_csv("./tkudata/課程資料/2-1開課資料.csv", index = False, encoding = "utf_8_sig")
df = df[df['req_ele_type'] == 'C']
df = df[df['yr'] == 107]
print(df[df['yr'] == 107]['ch_cos_name'].nunique())

# df.to_csv("./data/dfcip.csv", index = False, encoding = "utf_8_sig")
