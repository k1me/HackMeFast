from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.utils.query import execute_query

router = APIRouter()


# itt az elgondolás az, hogy a sys_admin jelszavát megváltoztassuk, de egyelőre még nincs implementálva kliens oldalon a http.post
@router.post("/6")
async def sys_admin_update(username: str):
    try:
        query = f"INSERT INTO login_logs (username) VALUES ('{username}')"
        result = execute_query(query, 6, fetch=False)

        return {"message": "Naplózva!"}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
