import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.utils import shuffle
from sklearn.decomposition import PCA

df = pd.read_csv("./tkudata/學生資料/1-3學生各科成績(期中).csv")

delreqeletype = df.index[df["req_ele_type"] == "A"]
df = df.drop(index=delreqeletype)
df.reset_index(inplace=True, drop=True)
# print(df)

# one hot encoding
df_ch_cos_name = df["ch_cos_name"]
df_stu_no_n = df["stu_no_n"]
ndf = pd.DataFrame(columns=["id", "course"],
                   index=[i for i in range(len(df_stu_no_n))])
ndf["id"] = df_stu_no_n
ndf["course"] = df_ch_cos_name
ndf = ndf.drop(index=0)
ndf.reset_index(inplace=True, drop=True)
ndf = shuffle(ndf)
ndf = ndf[:20000]
# print(ndf)
enc = OneHotEncoder(dtype=np.float32)
le = LabelEncoder()
for col in ndf[["id", "course"]]:
    ndf[col] = le.fit_transform(ndf[col])
print(ndf)
ndf_one = enc.fit_transform(ndf).toarray()
ndf_one = pd.DataFrame(ndf_one)
# ndf_one = pd.get_dummies(ndf)

print(ndf_one)

# ndf.to_csv("./data/ndf.csv",index = False)
ndf_one.to_csv("./data/ndfone.csv", index=False)
