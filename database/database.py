import pandas as pd

df_cs = pd.read_csv('../data/ndf107cs.csv')
ndf = pd.read_csv('../data/ndf107.csv')
ndf_course = pd.read_csv('../data/ndf107course.csv')


df_cs.to_json("ndf107cs.json",orient='values' )
ndf.to_json("ndf107.json", orient='table', index=False, force_ascii=False)
ndf_course.to_json("ndf107course.json", orient='table', index=False, force_ascii=False)
