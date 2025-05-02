from fastapi import APIRouter
from fastapi.responses import JSONResponse
import sqlite3
from app.config import DB_PATH

router = APIRouter()

@router.get("/2")
async def vulnerable_union(username: str):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        query = f"SELECT username FROM users WHERE username LIKE '%{username}%'"
        cursor.execute(query)
        result = cursor.fetchall()

        return {"results": result}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()