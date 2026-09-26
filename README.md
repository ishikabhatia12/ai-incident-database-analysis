AI helped create this file

# AI Incident Database Analysis

## Overview
This project analyzes publicly documented AI incidents from the AI Incident Database (https://incidentdatabase.ai/) to compare how the mechanisms behind AI harm changed between 2024 and 2025.

The analysis distinguishes between intentional human misuse, unintentional human-caused harm, intentional risks involving AI behavior, and unintentional AI system failures. It is intended to help policymakers consider where regulatory oversight should concentrate, including misuse prevention, pre-deployment testing, post-deployment monitoring, and accountability for organizations deploying AI.

## Research Question
Is the locus of AI harm shifting from intentional human misuse toward unintentional failures of deployed AI systems and if so, what does that imply for where regulatory oversight should concentrate (pre-deployment testing vs. post-deployment monitoring vs. deployer accountability)?

## Intended Audience
This analysis is intended for policymakers, regulators, and others interested in AI governance. It examines whether documented AI harms appear more strongly associated with deliberate misuse or unexpected system failures.

The findings can help frame—but cannot independently determine—which regulatory interventions will be most effective.

## Dataset
The project uses publicly available data from the AI Incident Database, which documents reported incidents in which AI systems caused or contributed to real-world harm.

The analysis focuses on incidents recorded for 2024 and 2025.

### Citation
McGregor, S. (2021). Preventing Repeated Real World AI Failures by Cataloging Incidents: The AI Incident Database. Proceedings of the AAAI Conference on Artificial Intelligence, 35(17), 15458–15463. https://doi.org/10.1609/aaai.v35i17.17817. Data accessed September 2026 via https://incidentdatabase.ai.

### Why EDA is limited to "relevant columns"
EDA.py immediately narrows the full dataset down to six columns before doing any analysis:


Incident ID — Unique identifier; needed to count incidents and confirm no duplicates
year — Splits the dataset into the 2024 and 2025 subsets this analysis compares
deployer — Used to identify top repeat deployers
harmed — Identifies who bears the harm, for framing policy stakes
Responsible Entity — Human vs. AI; one input to Incident Mechanism
Intent — Intentional vs. unintentional; the other input to Incident Mechanism

Every other column in the raw AIID export (free-text descriptions, report URLs, editor metadata, risk/harm taxonomies, etc.) is dropped at the start rather than carried through the pipeline. This keeps the dataset focused on exactly the fields the research question depends on, and avoids treating irrelevant or high-missingness columns as if they mattered for this analysis. Furthermore, it helps ensure the EDA is clean and not overly complicated by a very large dataset, where not all variables are the point of focus for the research question.

### EDA to Feature Engineering
All six relevant columns get explored in EDA.py, but they don't all carry equal weight for the research question. After running the initial descriptive statistics, the clearest and most policy-relevant pattern was the interaction between Intent and Responsible Entity: whether harm was caused on purpose or by accident, crossed with whether a human or an AI system was the responsible party. That 2×2 split maps directly onto the four regulatory levers named in the research question (misuse prevention, pre-deployment testing, post-deployment monitoring, deployer accountability) in a way no other single variable does — which is why it became the one engineered feature in this project, Incident Mechanism.

Deployer and harmed were deliberately not folded into a similar engineered variable:

Deployer describes where incidents cluster (are they concentrated among a few repeat organizations, or spread thin?) — a useful, separate question from why harm occurred, so it is left out
Harmed describes who bears the impact, which is valuable context for framing stakes but doesn't bear on the intentional-vs-unintentional, human-vs-AI question the research is centered on. It's reported in EDA (top harmed groups per year) but isn't carried into a new feature.

In short: Incident Mechanism exists because it was the variable that spoke most directly to the research question; deployer and harmed stayed as straightforward descriptive counts because collapsing them into Incident Mechanism would have blurred two different questions ("why did this happen" vs. "who did it affect / who keeps causing it") into one column.


## Methodology

### Exploratory Data Analysis
The exploratory analysis:

Loads the raw data and restricts it to the relevant columns above
Reports dataset shape and descriptive statistics
Confirms the number of unique incident IDs
Splits the data into df24 and df25 by year
Counts incidents recorded in each year
Identifies the most frequently listed deployers per year
Examines harmed groups per year
Compares Responsible Entity distributions per year
Computes Intent value counts per year (intentional vs. unintentional)

This stage only explores and prints — it does not modify or save any files. df24 and df25 are created here and reused by the next two stages.

### Feature Engineering
Imports EDA to reuse df24/df25, then adds one new column:

Incident Mechanism — a single categorical column that combines Responsible Entity and Intent into four mutually exclusive buckets:
1. Intentional human misuse
2. Unintentional human-caused harm
3. Intentional risk involving AI behavior
4. Unintentional AI failure

These two source columns are combined into one because the research question is specifically about the joint pattern of "who" (human/AI) and "why" (intentional/unintentional) — tracking them separately would require cross-tabulating two columns for every comparison in this project, whereas Incident Mechanism lets every downstream value_counts() and chart operate on one variable.

### Preprocessing
Imports EDA again (reusing the same df24/df25 objects, now carrying the columns added in step 2), then:

1. Drops Responsible Entity and Intent, since Incident Mechanism now captures the same information without redundancy
2. Saves the cleaned DataFrames to data/df24_clean.csv and data/df25_clean.csv


## Visualizations
1. Loads the two clean CSVs
2. Converts each year's Incident Mechanism counts to a percentage of that year's total (so a year with more overall incidents doesn't visually dominate every category)
3. Plots a grouped bar chart comparing 2024 vs. 2025 across all four mechanism categories


## Getting Started

### Prerequisites
Python 3.9 or later
Git

### Installation
Clone the repository:

git clone https://github.com/ishikabhatia12/ai-incident-database-analysis.git
cd ai-incident-database-analysis

Create and activate a virtual environment:

python3 -m venv .venv
source .venv/bin/activate

For Windows PowerShell:

.\.venv\Scripts\Activate.ps1

Install the required dependencies:

pip install -r requirements.txt

### Requirements
The analysis uses:
1. pandas
2. matplotlib

### How to Run
Run the full pipeline in one step from the project root:

python main.py

This executes, in order: EDA.py → Feature_Engineering.py → Preprocessing.py → yearly_incident_visualization.py. Running main.py will:

Print the EDA output (dataset shape, descriptive stats, top deployers, harmed groups, etc.) to the console
Write data/df24_clean.csv and data/df25_clean.csv
Open a window with the 2024 vs. 2025 comparison chart

