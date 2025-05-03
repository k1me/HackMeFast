import sqlite3
import os
import json
import random
import string
from app.config import DB_PATH, NUM_SQLI_TASKS, SECRETS_FILE


def random_string(length=8):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


def init_db(task_id):
    db_path = os.path.join(DB_PATH, f"users_{task_id}.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        """
                   CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        role TEXT NOT NULL
                        )                 
                   """
    )
    
    cursor.execute("DELETE FROM users")
    conn.commit()
    
    admin_pw = random_string()
    flag = f"FLAG{{task{task_id}_{random_string(8)}}}"

    cursor.execute(
        "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
        ("admin", admin_pw, "admin"),
    )
    cursor.execute(
        "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
        ("flagholder", flag, "user"),
    )
    cursor.execute(
        "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
        ("user1", random_string(), "user"),
    )
    cursor.execute(
        "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
        ("user2", random_string(), "user"),
    )

    conn.commit()
    conn.close()

    return {"task_id": task_id, "admin_password": admin_pw, "flag": flag}


def seed_all():
    if not os.path.exists(DB_PATH):
        os.makedirs(DB_PATH)

    all_secrets = []
    for task_id in range(1, NUM_SQLI_TASKS + 1):
        print(f"Task {task_id} seedelése...")
        secrets = init_db(task_id)
        all_secrets.append(secrets)

    with open(SECRETS_FILE, "w") as f:
        json.dump(all_secrets, f, indent=4)

    print("A seedelés befejeződött.")


if __name__ == "__main__":
    seed_all()
