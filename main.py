print("test")
print("2")

import pandas as pd

# pd.read_csv("")
disruption_data = pd.read_csv('data/disruptions-2025.csv')
long_disruptions = disruption_data[disruption_data["duration_minutes"] > 200]
print(long_disruptions)