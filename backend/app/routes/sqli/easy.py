from fastapi import APIRouter
from fastapi.responses import JSONResponse
import sqlite3
from app.config import DB_PATH

router = APIRouter()


@router.get("/search")
async def vulnerable_query_easy(username: str):

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        query = f"SELECT * FROM users WHERE username = '{username}'"
        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            return {"status": "success", "data": result}
        else:
            return {"status": "no result"}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    finally:
        if cursor and conn:
            cursor.close()
            conn.close()
