from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.utils.query import execute_query

router = APIRouter()


@router.get("/5")
async def waf_bypass(username: str, password: str):
    forbidden = ["or", "=", "/*", "'--", "' --", "'  -"]
    try:
        if any(fb in username.lower() for fb in forbidden) or any(
            fb in password.lower() for fb in forbidden
        ):
            return {"message": "Tiltott karaktert használtál!"}

        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        result = execute_query(query, 5)

        if result[0][1] == "admin":
            return {"message": "Flag: FLAG{waf_bypass_success}"}
        elif result:
            return {"message": f"Üdv újra {username}!"}
        else:
            return {"message": "Nincs ilyen felhasználó-jelszó kombináció!"}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
