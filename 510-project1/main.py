#AI helped generate this code
"""
Main entry point for the AI Incident Database pipeline.
 
Running this file executes each stage in order:
1. EDA.py                           -> loads raw data, explores it, creates EDA.df24 / EDA.df25
2. Feature_Engineering.py           -> adds deployer_incident_count + Incident Mechanism
3. Preprocessing.py                 -> drops redundant columns, saves clean CSVs
4. yearly_incident_visualization.py -> loads the clean CSVs and plots the comparison
"""
 
import EDA
import Feature_Engineering
import Preprocessing
import yearly_incident_visualization
 
print("Pipeline complete: df24_clean.csv and df25_clean.csv saved, chart displayed.")