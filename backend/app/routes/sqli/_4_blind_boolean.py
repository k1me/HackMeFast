from fastapi import APIRouter
from fastapi.responses import JSONResponse
import sqlite3
from app.config import DB_PATH

router = APIRouter()


@router.get("/4")
async def blind_boolean(username: str):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        query = f"SELECT 1 FROM users WHERE username = '{username}'"
        cursor.execute(query)

        if cursor.fetchone():
            return {"result": "Van ilyen felhasználó"}
        else:
            return {"result": "Nincs ilyen felhasználó"}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()