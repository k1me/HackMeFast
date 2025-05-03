from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.utils.query import execute_query

router = APIRouter()


@router.get("/3")
async def data_leak(username: str):
    try:
        query = f"SELECT username FROM users WHERE id = {username}"
        result = execute_query(query, 3, fetch_one=True)

        if result:
            return {"username": result[0]}
        else:
            return {"message": "Nincs ilyen felhasználó!"}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
