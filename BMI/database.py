import sqlite3

DB_NAME = "bmi_data.db"

def init_db():
    """Creates the table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT DEFAULT CURRENT_TIMESTAMP,
            weight REAL,
            height REAL,
            bmi REAL,
            category TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_record(weight, height, bmi, category):
    """Saves a new BMI record."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO history (weight, height, bmi, category)
        VALUES (?, ?, ?, ?)
    ''', (weight, height, bmi, category))
    conn.commit()
    conn.close()

def fetch_history():
    """Gets the last 10 records."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT date, bmi, category FROM history ORDER BY id DESC LIMIT 10')
    data = cursor.fetchall()
    conn.close()
    return data

def fetch_all_bmi_for_graph():
    """Gets all BMI values for plotting."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT id, bmi FROM history')
    data = cursor.fetchall()
    conn.close()
    return data