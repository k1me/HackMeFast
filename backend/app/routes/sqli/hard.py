from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
import sqlite3
from app.config import DB_PATH

router = APIRouter()


@router.get("/search")
async def vulnerable_query_hard(request: Request):
    username = request.query_params.get("username", "")

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        query = f"SELECT username, role FROM users WHERE role='user' AND username = '{username}'"
        cursor.execute(query)

        results = cursor.fetchall()

        if not results:
            return JSONResponse(status_code=404, content={"error": "No results found"})

        return {"result": [{"username": row[0], "role": row[1]} for row in results]}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    finally:
        if cursor and conn:
            cursor.close()
            conn.close()
