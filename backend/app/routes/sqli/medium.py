from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
import sqlite3
from app.config import DB_PATH

router = APIRouter()


@router.get("/search")
async def vulnerable_query_medium(request: Request):
    username = request.query_params.get("username", "")

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        query = f"SELECT * FROM users WHERE username ='{username}'"
        cursor.execute(query)

        results = cursor.fetchall()

        return {"result": results}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    finally:
        if cursor and conn:
            cursor.close()
            conn.close()
