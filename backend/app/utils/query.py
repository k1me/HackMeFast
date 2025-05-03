import sqlite3
import os
from fastapi.responses import JSONResponse
from app.config import DB_PATH


def execute_query(
    query: str, task_id: int, fetch_one: bool = False, fetch: bool = True
):
    conn = None
    cursor = None

    try:
        conn = sqlite3.connect(os.path.join(DB_PATH, f"users_{task_id}.db"))
        cursor = conn.cursor()
        cursor.execute(query)

        if fetch:
            return cursor.fetchone() if fetch_one else cursor.fetchall()
        else:
            conn.commit()
            result = None

        return result

    except Exception:
        raise

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
