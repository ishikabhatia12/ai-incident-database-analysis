#AI helped generate this code

import pandas as pd
import EDA

df24 = EDA.df24
df25 = EDA.df25

#Drop responsible entity and intent columns because incident mechanisms captures content in one column
df24 = df24.drop(columns=["Responsible Entity", "Intent"])
df25 = df25.drop(columns=["Responsible Entity", "Intent"])

#Save new DFs as CSVs
df24.to_csv("data/df24_clean.csv", index=False)
df25.to_csv("data/df25_clean.csv", index=False)
