from fastapi import APIRouter
from fastapi.responses import JSONResponse
import sqlite3
from app.config import DB_PATH

router = APIRouter()


@router.get("/5")
async def waf_bypass(username: str, password: str):
    conn = None
    cursor = None
    try:
        if any(
            x in username.lower() for x in ["or", "=", "/*", "'--", "' --", "'  -"]
        ) or any(
            x in password.lower() for x in ["or", "=", "/*", "'--", "' --", "'  -"]
        ):
            return {"message": "Tiltott karaktert használtál!"}

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)
        result = cursor.fetchall()

        if result[0][1] == "admin":
            return {"message": "Flag: FLAG{waf_bypass_success}"}
        elif result:
            return {"message": f"Üdv újra {username}!"}
        else:
            return {"message": "Nincs ilyen felhasználó-jelszó kombináció!"}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
