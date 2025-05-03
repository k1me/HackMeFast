from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.utils.query import execute_query

router = APIRouter()


@router.get("/1")
async def vulnerable_query_easy(username: str, password: str):

    try:
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

        result = execute_query(query, 1)

        if result:
            first_row = result[0]
            if first_row[1] == "admin":
                return {"status": "success", "flag": "FLAG{pelda_flag}"}
            else:
                return {"status": "success", "data": result}
        else:
            return {"message": "Nem megfelelő bejelentkezési adatok"}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
