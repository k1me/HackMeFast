from fastapi import APIRouter
from fastapi.responses import JSONResponse
import sqlite3
from app.config import DB_PATH

router = APIRouter()

# itt az elgondolás az, hogy a sys_admin jelszavát megváltoztassuk, de egyelőre még nincs implementálva kliens oldalon a http.post 
@router.post("/6")
async def sys_admin_update(username: str):
    conn = None
    cursor = None
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        query = f"INSERT INTO login_logs (username) VALUES ('{username}')"
        cursor.execute(query)
        conn.commit()

        return {"message": "Naplózva!"}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()