from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
import sqlite3
from app.config import DB_PATH

router = APIRouter()

FORBIDDEN = ["'", '"', "--", ";", "#"]


def is_input_safe(value: str) -> bool:
    lower_val = value.lower()
    return not any(bad in lower_val for bad in FORBIDDEN)


@router.get("/search")
async def vulnerable_query_medium(username: str, password: str):

    if not is_input_safe(username) or not is_input_safe(password):
        return JSONResponse(status_code=422, content={"error": "Invalid input"})

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)

        result = cursor.fetchall()

        if result:
            return {"status": "success", "data": result}
        else:
            return {"status": "no result"}
        
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
