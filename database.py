import sqlite3
import pandas as pd

def export_to_csv(file_name="consultations.csv"):
    conn = sqlite3.connect("health.db")
    df = pd.read_sql_query("SELECT * FROM consultations", conn)
    df.to_csv(file_name, index=False)
    conn.close()
    print(f"\n✅ All consultations exported to {file_name}")

def create_database():
    conn = sqlite3.connect("health.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS consultations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT,
            symptoms TEXT,
            predicted_disease TEXT,
            severity TEXT,
            doctor TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_record(name, symptoms, disease, severity, doctor):
    conn = sqlite3.connect("health.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO consultations (user_name, symptoms, predicted_disease, severity, doctor)
        VALUES (?, ?, ?, ?, ?)
    """, (name, symptoms, disease, severity, doctor))

    conn.commit()
    conn.close()
def get_all_records():
    conn = sqlite3.connect("health.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM consultations")
    rows = cursor.fetchall()
    conn.close()
    return rows
