import sqlite3

DB_PATH = "backend/users.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL
                        )
                    """)
    
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS sessions (
                        session_id TEXT PRIMARY KEY,
                        username TEXT NOT NULL,
                        FOREIGN KEY (username) REFERENCES users(username)
                    )
                    """)
    
    cursor.execute("INSERT OR IGNORE INTO users(username, password) VALUES ('admin', '1234')")
    cursor.execute("INSERT OR IGNORE INTO users(username, password) VALUES ('user', 'password')")
    
    conn.commit()
    conn.close()
    
    
init_db()
