import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("../tkudata/學生資料/1-3學生各科成績(期中).csv")

delreqeletype = df.index[df["req_ele_type"] == "A"]
df = df.drop(index = delreqeletype)

# one hot encoding
df_ch_cos_name = df[df['yr'] == '107']["ch_cos_name"].reset_index(drop = True)
df_stu_no_n = df[df['yr'] == '107']["stu_no_n"].reset_index(drop = True)
ndf = pd.DataFrame(columns = ["id", "course"],
                   index = [i for i in range(len(df_stu_no_n))])
ndf["id"] = df_stu_no_n
ndf["course"] = df_ch_cos_name
df_ch_cos_name_unique = df[df['yr'] == '107']["ch_cos_name"].reset_index(drop = True).unique()
ndf_course = pd.DataFrame(columns = ["course"],
                          index = [i for i in range(len(df_ch_cos_name_unique))])
ndf_course["course"] = df_ch_cos_name_unique

# print(ndf_course)
ndf_course.to_csv("../data/ndf107course.csv", index = False, encoding = "utf_8_sig")

ndf_one = pd.get_dummies(ndf['course'])
ndf_one.set_index(df_stu_no_n, inplace = True)

# Cosine Similarity
ndf_one = pd.read_csv('../data/ndf107one.csv')
ndf_one = ndf_one.groupby(ndf_one['stu_no_n']).sum()
ndf_one = ndf_one.mask(ndf_one - 2 == 0, 1)
ndf_one = cosine_similarity(ndf_one, ndf_one, dense_output=False)
ndf_cs = pd.DataFrame(ndf_one)

# ndf.to_csv("../data/ndf107.csv", index = False, encoding = "utf_8_sig")

# transpose
df = pd.read_csv("../data/ndf107one.csv")
dfT = df.T
# print(dfT)
dfT.to_csv("../data/ndf107T.csv", index = True, encoding = "utf_8_sig")
df = pd.read_csv("../data/ndf107T.csv")
df = df.drop([0])
print(df)
df.to_csv("../data/ndf107T.csv", index = False, encoding = "utf_8_sig")
