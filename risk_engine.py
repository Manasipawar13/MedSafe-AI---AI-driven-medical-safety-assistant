def check_interactions(medicines):

    interactions = []

    dangerous_pairs = [
        ("ibuprofen", "aspirin"),
        ("paracetamol", "alcohol"),
        ("amoxicillin", "methotrexate"),
        ("warfarin", "aspirin")
    ]

    for m1 in medicines:
        for m2 in medicines:

            if (m1, m2) in dangerous_pairs or (m2, m1) in dangerous_pairs:

                interactions.append(
                    f"⚠ Warning: {m1} and {m2} may interact dangerously."
                )

    return interactions