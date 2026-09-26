#AI helped generate this code

import matplotlib.pyplot as plt
import pandas as pd

df24 = pd.read_csv("data/df24_clean.csv")
df25 = pd.read_csv("data/df25_clean.csv")

# Convert each year's counts to a % of that year's total, so a year with more overall incidents doesn't visually dominate every category
counts_24 = df24["Incident Mechanism"].value_counts(normalize = True)*100
counts_25 = df25["Incident Mechanism"].value_counts(normalize = True)*100

comparison = pd.DataFrame({
    "2024": counts_24,
    "2025": counts_25
})

comparison = comparison.loc[
    ["Intentional human misuse","Intentional risk involving AI behavior", "Unintentional human-caused harm","Unintentional AI failure"]
]

# Change labels only after selecting the data
comparison.index = [
    "Intentional\nhuman misuse",
    "Intentional risk involving\nAI behavior",
    "Unintentional\nhuman-caused harm",
    "Unintentional\nAI failure"
]

comparison.plot(kind="bar",figsize=(12, 6),color=["#0A0AF5", "#4786AD"])

plt.title("Intentional Human Misuse vs. Unintentional AI misuse", fontweight='bold', fontsize=16)
plt.xlabel("Incident Mechanism (percent of yearly total)", fontweight='bold', fontsize = 12)
plt.ylabel("Number of Incidents", fontweight='bold',fontsize=12 )
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()
