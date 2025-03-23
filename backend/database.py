import sqlite3

DB_NAME = "leads.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            score INTEGER
        )
    """)
    conn.commit()
    conn.close()

def add_lead(name, email, score):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO leads (name, email, score) VALUES (?, ?, ?)", (name, email, score))
    conn.commit()
    lead_id = cursor.lastrowid
    conn.close()
    return lead_id

def get_leads():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM leads")
    leads = cursor.fetchall()
    conn.close()
    return [{"id": l[0], "name": l[1], "email": l[2], "score": l[3]} for l in leads]
