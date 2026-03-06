from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.parser import load_patient_records
from app.database import create_database, insert_records
from app.vector_store import build_vector_index
from app.retriever import hybrid_retrieval
from app.llm import generate_answer

app = FastAPI()

# Load data at startup
records = load_patient_records()

create_database()
insert_records(records)

build_vector_index()


class QueryRequest(BaseModel):
    mrd_number: str
    query: str


@app.post("/query")
def query_patient(request: QueryRequest):

    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    results = hybrid_retrieval(request.query, request.mrd_number)

    if not results:
        raise HTTPException(status_code=404, detail="No relevant clinical information found")

    context = "\n".join(results)

    try:
        answer = generate_answer(context, request.query)
    except Exception:
        raise HTTPException(status_code=500, detail="LLM inference error")

    confidence = "High" if len(results) > 3 else "Medium"

    return {
        "mrd_number": request.mrd_number,
        "answer": answer,
        "confidence": confidence
    }