import sqlite3

DB_PATH = "database/patients.db"


def create_database():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS records (
            mrd_number TEXT,
            visit_id TEXT,
            document_type TEXT,
            text TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_records(records):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for r in records:

        cursor.execute("""
            INSERT INTO records VALUES (?, ?, ?, ?)
        """, (
            r["mrd_number"],
            r["visit_id"],
            r["document_type"],
            r["text"]
        ))

    conn.commit()
    conn.close()