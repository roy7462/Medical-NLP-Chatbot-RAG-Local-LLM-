import sqlite3
from app.vector_store import semantic_search

DB_PATH = "database/patients.db"


def sql_retrieval(mrd_number):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    rows = cursor.execute(
        "SELECT text FROM records WHERE mrd_number = ?",
        (mrd_number,)
    ).fetchall()

    conn.close()

    return [r[0] for r in rows]


def hybrid_retrieval(query, mrd_number):

    sql_docs = sql_retrieval(mrd_number)

    vector_results = semantic_search(query)

    vector_docs = [r[3] for r in vector_results if r[0] == mrd_number]

    return sql_docs + vector_docs