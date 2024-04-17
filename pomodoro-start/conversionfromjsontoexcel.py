import pandas as pd
import json

# Read the JSON file
with open('d.json', 'r') as f:
    json_data = json.load(f)

# Parse JSON data
# Assuming json_data is a list of dictionaries
# You may need to adjust this part based on the structure of your JSON data
df = pd.DataFrame(json_data)

# Write data to Excel file
df.to_excel('output.xlsx', index=False)
