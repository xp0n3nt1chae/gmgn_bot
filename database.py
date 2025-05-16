import sqlite3

conn = sqlite3.connect('tokens.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tokens (
    timestamp TEXT,
    pair_name TEXT,
    chain_id TEXT,
    price_usd REAL,
    trend TEXT,
    rugcheck_url TEXT,
    bubblemaps_url TEXT
)
''')

def log_token(data):
    cursor.execute('''
        INSERT INTO tokens (timestamp, pair_name, chain_id, price_usd, trend, rugcheck_url, bubblemaps_url)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', data)
    conn.commit()