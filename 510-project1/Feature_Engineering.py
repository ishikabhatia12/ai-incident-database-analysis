#AI helped generate this code

import pandas as pd
import EDA

df24 = EDA.df24
df25 = EDA.df25

#Create new column to identify combination of intentional or unintential and human or AI for df 24
df24.loc[
    (df24["Responsible Entity"] == "Human") &
    (df24["Intent"] == "Intentional"),
    "Incident Mechanism"
] = "Intentional human misuse"

df24.loc[
    (df24["Responsible Entity"] == "Human") &
    (df24["Intent"] == "Unintentional"),
    "Incident Mechanism"
] = "Unintentional human-caused harm"

df24.loc[
    (df24["Responsible Entity"] == "AI") &
    (df24["Intent"] == "Unintentional"),
    "Incident Mechanism"
] = "Unintentional AI failure"

df24.loc[
    (df24["Responsible Entity"] == "AI") &
    (df24["Intent"] == "Intentional"),
    "Incident Mechanism"
] = "Intentional risk involving AI behavior"



#Create new column to identify combination of intentional or unintential and human or AI for df 25
df25.loc[
    (df25["Responsible Entity"] == "Human") &
    (df25["Intent"] == "Intentional"),
    "Incident Mechanism"
] = "Intentional human misuse"

df25.loc[
    (df25["Responsible Entity"] == "Human") &
    (df25["Intent"] == "Unintentional"),
    "Incident Mechanism"
] = "Unintentional human-caused harm"

df25.loc[
    (df25["Responsible Entity"] == "AI") &
    (df25["Intent"] == "Unintentional"),
    "Incident Mechanism"
] = "Unintentional AI failure"

df25.loc[
    (df25["Responsible Entity"] == "AI") &
    (df25["Intent"] == "Intentional"),
    "Incident Mechanism"
] = "Intentional risk involving AI behavior"