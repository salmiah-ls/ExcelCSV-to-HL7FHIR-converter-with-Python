def transform_row(row, mapping):
    test_name = mapping.get(row['test'], row['test'])

    fhir = {
        "resourceType": "Observation",
        "status": "final",

        "subject": {
            "reference": f"Patient/{row['patient_id']}"
        },

        "code": {
            "text": test_name
        },

        "valueQuantity": {
            "value": float(row['result']),
            "unit": row['unit']
        },

        "effectiveDateTime": row['date']
    }

    return fhir
