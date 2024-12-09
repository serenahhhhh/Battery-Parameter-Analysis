import pandas as pd
import plotly.express as px

# Load the dataset
file_path = r"C:\Users\Lenovo\OneDrive\Desktop\assignmentr\metadata.csv"  # Replace with your file path
dataset = pd.read_csv(file_path)

# Convert columns to numeric if necessary
dataset['Re'] = pd.to_numeric(dataset['Re'], errors='coerce')
dataset['Rct'] = pd.to_numeric(dataset['Rct'], errors='coerce')

# Drop rows with missing values in 'Re' and 'Rct'
filtered_data = dataset.dropna(subset=['Re', 'Rct'])

# Optional: Drop missing values for other columns
filtered_data = filtered_data.dropna(subset=['test_id', 'ambient_temperature'])

# Plot for Estimated Electrolyte Resistance (Re) over test cycles
fig1 = px.scatter(
    filtered_data,
    x="test_id",  # Replace 'test_id' with a column that represents cycles or time
    y="Re",
    color="ambient_temperature",  # Optional: Color by temperature
    title="Estimated Electrolyte Resistance (Re) Over Cycles",
    labels={"test_id": "Test Cycle", "Re": "Electrolyte Resistance (Ohms)"},
    trendline="lowess",  # Optional: Add a trendline
)
fig1.update_traces(marker=dict(size=6))  # Adjust marker size
fig1.show()

# Plot for Estimated Charge Transfer Resistance (Rct) over test cycles
fig2 = px.scatter(
    filtered_data,
    x="test_id",  # Replace 'test_id' with a column that represents cycles or time
    y="Rct",
    color="ambient_temperature",  # Optional: Color by temperature
    title="Estimated Charge Transfer Resistance (Rct) Over Cycles",
    labels={"test_id": "Test Cycle", "Rct": "Charge Transfer Resistance (Ohms)"},
    trendline="lowess",  # Optional: Add a trendline
)
fig2.update_traces(marker=dict(size=6))  # Adjust marker size
fig2.show()
