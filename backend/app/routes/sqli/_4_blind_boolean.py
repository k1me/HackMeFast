from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.utils.query import execute_query

router = APIRouter()


@router.get("/4")
async def blind_boolean(username: str):
    try:
        query = f"SELECT 1 FROM users WHERE username = '{username}'"
        result = execute_query(query, 4, fetch_one=True)

        if result:
            return {"result": "Van ilyen felhasználó!"}
        else:
            return {"result": "Nincs ilyen felhasználó!"}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
