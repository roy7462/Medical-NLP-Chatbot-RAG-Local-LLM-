import json
import os
from bs4 import BeautifulSoup


def clean_html(text):

    if not text:
        return ""

    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text(separator=" ").strip()


def load_patient_records(data_folder="data"):

    patient_data = []

    for file in os.listdir(data_folder):

        if file.endswith(".json"):

            path = os.path.join(data_folder, file)

            with open(path, "r", encoding="utf-8") as f:
                records = json.load(f)

            for record in records:

                cleaned_text = clean_html(record.get("description", ""))

                patient_data.append({
                    "mrd_number": record.get("mrd_number"),
                    "visit_id": record.get("visit_id"),
                    "document_type": record.get("document_type"),
                    "text": cleaned_text
                })

    return patient_data