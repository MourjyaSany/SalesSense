import sqlite3

def init_db():
    conn = sqlite3.connect('leads.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            score INTEGER
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Database initialized.")
