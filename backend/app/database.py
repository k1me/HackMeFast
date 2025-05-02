import sqlite3

DB_PATH = "backend/app/database/users.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        role TEXT NOT NULL
                        )
                    """)
    
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS sessions (
                        session_id TEXT PRIMARY KEY,
                        username TEXT NOT NULL,
                        FOREIGN KEY (username) REFERENCES users(username)
                    )
                    """)
    
    cursor.execute("INSERT OR IGNORE INTO users(username, password, role) VALUES ('admin', '1234', 'admin')")
    cursor.execute("INSERT OR IGNORE INTO users(username, password, role) VALUES ('user', 'password', 'user')")
    cursor.execute("INSERT OR IGNORE INTO users(username, password, role) VALUES ('admin', 'asd123',  'admin')")
    cursor.execute("INSERT OR IGNORE INTO users(username, password, role) VALUES ('user1', 'asd321', 'user')")
    cursor.execute("INSERT OR IGNORE INTO users(username, password, role) VALUES ('user2', 'dsa123' , 'user')")
    cursor.execute("INSERT OR IGNORE INTO users(username, password, role) VALUES ('user3', 'dsadsa' , 'user')")
    cursor.execute("INSERT OR IGNORE INTO users(username, password, role) VALUES ('flagholder', 'FLAG{leaked_data_pelda_flag}' , 'user')")
    
    conn.commit()
    conn.close()
    
    
init_db()
