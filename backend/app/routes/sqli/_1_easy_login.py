from fastapi import APIRouter
from fastapi.responses import JSONResponse
import sqlite3
from app.config import DB_PATH

router = APIRouter()


@router.get("/1")
async def vulnerable_query_easy(username: str, password: str):

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)

        result = cursor.fetchall()

        if result:
            first_row = result[0]
            if first_row[1] == "admin":
                return {"status": "success", "flag": "FLAG{pelda_flag}"}
            else:
                return {"status": "success", "data": result}
        else:
            return {
                "status": "no result",
                "message": "Nem megfelelő bejelentkezési adatok",
            }

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
