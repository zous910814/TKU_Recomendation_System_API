import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances

df = pd.read_csv("./tkudata/學生資料/1-3學生各科成績(期中).csv")

delreqeletype = df.index[df["req_ele_type"] == "A"]
df = df.drop(index=delreqeletype)
df.reset_index(inplace=True, drop=True)
# print(df)

# one hot encoding
df_ch_cos_name = df[df['yr'] == '107']["ch_cos_name"].reset_index(drop=True)
df_stu_no_n = df[df['yr'] == '107']["stu_no_n"].reset_index(drop=True)
ndf = pd.DataFrame(columns=["id", "course"],
                   index=[i for i in range(len(df_stu_no_n))])
ndf["id"] = df_stu_no_n
ndf["course"] = df_ch_cos_name

# print(ndf['id'].nunique())

ndf_one = pd.get_dummies(ndf['course'])
ndf_one.set_index(df_stu_no_n, inplace=True)
# print(ndf_one)

# ndf.to_csv("./data/ndf107.csv",index = False)
# ndf_one.to_csv("./data/ndf107one.csv", index=True, encoding="utf_8_sig")

ndf_one = pd.read_csv('./data/ndf107one.csv')
ndf_one = ndf_one.groupby(ndf_one['stu_no_n']).sum()
# print(ndf_one)
ndf_one = ndf_one.mask(ndf_one - 2 == 0, 1)
ndf_one = cosine_similarity(ndf_one, ndf_one, dense_output=False)
ndf_cs = pd.DataFrame(ndf_one)
# ndf_one = euclidean_distances(ndf_one)
# ndf_ed = pd.DataFrame(ndf_one)
# print(ndf_cs)

# ndf_cs.to_csv("./data/ndf107cs.csv", index=True, encoding="utf_8_sig")


def get_the_most_similar_movies(user_id, user_movie_matrix, num):
    user_vec = user_movie_matrix.loc[user_id].values
    sorted_index = np.argsort(user_vec)[:num]
    return list(user_movie_matrix.columns[sorted_index])

a = get_the_most_similar_movies(200,ndf_cs,6)
print(ndf.iloc[200])
print(ndf.iloc[a[1:]])