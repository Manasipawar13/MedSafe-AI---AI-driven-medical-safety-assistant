import pandas as pd

data = pd.read_csv("medicine_database.csv")

medicine_list = data["medicine"].str.lower().tolist()

def find_medicines(text):

    text = text.lower()

    detected = []

    for medicine in medicine_list:
        if medicine in text:
            detected.append(medicine)

    return detected