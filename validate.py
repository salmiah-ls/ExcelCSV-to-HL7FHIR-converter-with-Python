def validate_fhir(fhir):

    required_fields = [
        "resourceType",
        "status",
        "subject",
        "code",
        "valueQuantity"
    ]

    return all(field in fhir for field in required_fields)