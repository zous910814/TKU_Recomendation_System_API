import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)

ndf_cs=pd.read_csv("data/ndf107cs.csv", index=True, encoding="utf_8_sig")
ndf_cs.to_sql('data/ndf_cs', con=engine)