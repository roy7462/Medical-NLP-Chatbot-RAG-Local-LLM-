import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_answer(context, query):

    prompt = f"""
You are a clinical medical assistant.

Answer ONLY using the provided patient records.

Rules:
- Clinical tone only
- No assumptions
- No speculation
- If answer not found say: "Information not available in records"

Patient Records:
{context}

Question:
{query}

Answer:
"""

    payload = {
        "model": "phi3",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    data = response.json()

    if "response" not in data:
        raise Exception(f"Ollama error: {data}")

    return data["response"]