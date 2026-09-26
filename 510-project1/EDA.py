#AI helped generate this code

import pandas as pd

df = pd.read_csv("data/AIID.csv")

#EDA: General shape and structure

relevant_columns = [
    "Incident ID",
    "year",
    "deployer",
    "harmed",
    "Responsible Entity",
    "Intent"
]
 
df = df[relevant_columns]
 
print(df.head())
print(df.shape)

#identify number of unique incident IDs
unique_incident_ids = df['Incident ID'].nunique()
print(f"Number of unique incident IDs: {unique_incident_ids}")

#Create a new df for only 2024 incidents
df24 = df[df['year'] == 2024]
#First 5 rows of 2024 df
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

#count number of times in 2024 intent was intentional vs unintentional
intent_count_24 = df24['Intent'].value_counts()

#count number of times in 2025 intent was intentional vs unintentional
intent_count_25 = df25['Intent'].value_counts()

