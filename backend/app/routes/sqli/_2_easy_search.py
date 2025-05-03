from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.utils.query import execute_query

router = APIRouter()


@router.get("/2")
async def vulnerable_union(username: str):
    try:
        query = f"SELECT username FROM users WHERE username LIKE '%{username}%'"
        result = execute_query(query, 2)

        return {"results": result}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
