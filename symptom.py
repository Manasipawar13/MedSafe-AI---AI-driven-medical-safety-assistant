def calculate_risk(medicines):

    high_risk = ["aspirin", "ibuprofen"]
    medium_risk = ["naproxen"]
    
    risk_score = 0

    for med in medicines:
        if med in high_risk:
            risk_score += 2
        elif med in medium_risk:
            risk_score += 1

    if risk_score >= 3:
        return "High Risk"
    elif risk_score == 2:
        return "Moderate Risk"
    else:
        return "Low Risk"