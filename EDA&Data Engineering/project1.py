import pandas as pd

df = pd.read_csv("data/AIID.csv")

#EDA
print(df.head())
print(df.shape)
#identify number of unique incident IDs
unique_incident_ids = df['Incident ID'].nunique()
print(f"Number of unique incident IDs: {unique_incident_ids}")

#create a new df for only 2024 incidents
df24 = df[df['year'] == 2024]
#first 5 rows of 2024 df
print(df24.head())
#Descriptive stats for 2024 df
print("Descriptive statistics for all variables:")
print("")
print(df24.describe(include="all"))

#create a new df for only 2025 incidents 
df25 = df[df['year'] == 2025]
#Descriptive stats for 2024 df
#first 5 rows of 2025 df
print(df25.head())
print("Descriptive statistics for all variables:")
print("")
print(df25.describe(include="all"))


#identify number of incidents in 2024
print(f"Number of incidents in 2024: {len(df24)}")

#identify number of incidents in 2025
print(f"Number of incidents in 2025: {len(df25)}")

#identify total unique deployers in 2024
unique_deployers = df24['deployer'].nunique()
print(f"Total unique deployers in 2024: {unique_deployers}")

#identify top 3 most frequently mentioned deployers in 2024
top_deployers_2024 = df24['deployer'].value_counts().head(3)
print("Top 3 most frequently mentioned deployers in 2024:", top_deployers_2024)

#identify total unique deployers in 2025
unique_deployers_2025 = df25['deployer'].nunique()
print(f"Total unique deployers in 2025: {unique_deployers_2025}")

#identify top 3 most frequently mentioned deployers in 2025
top_deployers_2025 = df25['deployer'].value_counts().head(3)
print("Top 3 most frequently mentioned deployers in 2025:", top_deployers_2025)

#identify total unique harmed groups in 2024
unique_harmed_groups_2024 = df24['harmed'].nunique()
print(f"Total unique harmed groups in 2024: {unique_harmed_groups_2024}")

#identify top 3 most frequently harmed groups in 2024
top_harmed_groups_2024 = df24['harmed'].value_counts().head(3)
print("Top 3 most frequently harmed groups in 2024:", top_harmed_groups_2024)

#identify total unique harmed groups in 2025
unique_harmed_groups_2025 = df25['harmed'].nunique()
print(f"Total unique harmed groups in 2025: {unique_harmed_groups_2025}")

#identify top 3 most frequently harmed groups in 2025
top_harmed_groups_2025 = df25['harmed'].value_counts().head(3)
print("Top 3 most frequently harmed groups in 2025:", top_harmed_groups_2025)

#identify reponsible entity distribution in 2024
responsible_entity_24 = df24['Responsible Entity'].value_counts()
print(responsible_entity_24)

#identify responsible entity distribution in 2025
responsible_entity_25 = df25['Responsible Entity'].value_counts()
print(responsible_entity_25)

#identify top 3 risk domains in 2024
risk_domains_24 = df24['Risk Domain'].head(3)
print(risk_domains_24)

#identify top 3 risk domains in 2025
risk_domains_25 = df25['Risk Domain'].head(3)
print(risk_domains_25)





#Data Engineering

#Create a new column in each df that counts incident per deployer for given year
df24['deployer_incident_count'] = (df24.groupby("deployer")["Incident ID"].transform("count"))
df25['deployer_incident_count'] = (df25.groupby("deployer")["Incident ID"].transform("count"))

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
] = "Unintentional human misuse"

df24.loc[
    (df24["Responsible Entity"] == "AI") &
    (df24["Intent"] == "Unintentional"),
    "Incident Mechanism"
] = "Unintentional AI misuse"

df24.loc[
    (df24["Responsible Entity"] == "AI") &
    (df24["Intent"] == "Intentional"),
    "Incident Mechanism"
] = "Intentional human misuse"



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
] = "Unintentional human misuse"

df25.loc[
    (df25["Responsible Entity"] == "AI") &
    (df25["Intent"] == "Unintentional"),
    "Incident Mechanism"
] = "Unintentional AI misuse"

df25.loc[
    (df25["Responsible Entity"] == "AI") &
    (df25["Intent"] == "Intentional"),
    "Incident Mechanism"
] = "Intentional human misuse"


#Save new DFs as CSVs
df24.to_csv("data/df24_clean", index=False)
df25.to_csv("data/df25_clean", index=False)
