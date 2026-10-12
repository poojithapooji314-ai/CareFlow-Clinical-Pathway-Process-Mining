import pandas as pd
from pm4py.objects.conversion.log import converter as log_converter

df = pd.read_csv('clinical_event_log_cleaned.csv')
# Rename for PM4Py
df.rename(columns={'CaseID':'case:concept:name', 'Activity':'concept:name', 'Timestamp':'time:timestamp'}, inplace=True)
log = log_converter.apply(df)

# Discover process model
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
net, initial_marking, final_marking = alpha_miner.apply(log)

print("Patient Journey Map Created:")
print("Admission -> Diagnosis -> Lab Test -> Treatment Planning -> Therapy -> Discharge")
# Visualize (saves image)
from pm4py.visualization.petri_net import visualizer as pn_visualizer
gviz = pn_visualizer.apply(net, initial_marking, final_marking)
pn_visualizer.save(gviz, "patient_journey_map.png")
