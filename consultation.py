from diseases_data import diseases
from difflib import get_close_matches

def predict_diseases(user_symptoms, top_n=3):
    """
    Predict top N possible diseases based on symptoms.
    Returns a list of tuples: (disease_name, match_count)
    """
    user_symptoms = [sym.strip().lower() for sym in user_symptoms]

    disease_matches = []

    for disease, info in diseases.items():
        disease_symptoms = [s.lower() for s in info["symptoms"]]
        match_count = 0

        for sym in user_symptoms:
            if sym in disease_symptoms or get_close_matches(sym, disease_symptoms, cutoff=0.7):
                match_count += 1

        if match_count > 0:
            disease_matches.append((disease, match_count))

    # Sort by match count descending
    disease_matches.sort(key=lambda x: x[1], reverse=True)

    return disease_matches[:top_n]
