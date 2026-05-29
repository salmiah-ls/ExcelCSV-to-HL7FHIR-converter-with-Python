import pandas as pd
import json

from src.transform import transform_row
from src.validate import validate_fhir

def run_pipeline():

    # Load CSV
    df = pd.read_csv("data/raw/lab_data.csv")

    # Load mapping
    with open("config/mapping.json") as f:
        mapping = json.load(f)

    output = []

    for _, row in df.iterrows():

        # Convert row to FHIR
        fhir = transform_row(row, mapping)

        # Validate
        if validate_fhir(fhir):
            output.append(fhir)

    # Save JSON
    with open("data/output/fhir_output.json", "w") as f:
        json.dump(output, f, indent=2)

    print("FHIR conversion completed.")
