from fastapi import FastAPI, Form, Request, Response, Depends
from fastapi.responses import PlainTextResponse, HTMLResponse, JSONResponse
import os, secrets

app = FastAPI()
#-------------------| DIRECTORY TRAVERSAL |-------------------|

# ez a dir ahonnan ki szeretnenk olvasni a file tartalmat
BASE_DIR = "static_files"

#---------------read endpoint---------------
# input: file nev
# output: fajl tartalma, ha letezik, amugy error
@app.get("/read-file/")
async def read_file(filename: str):
    file_path = os.path.join(BASE_DIR, filename)
    
    try:
        with open(file_path, "r") as f:
            return PlainTextResponse(f.read())
    except FileNotFoundError:
        return {"error ": "File not found"}
        

#---------------delete endpoint---------------
# input: file nev
# output: sikeres torles visszajelzes, amugy error
@app.delete("/delete-file/")
async def delete_file(filename: str):
	file_path = os.path.join(BASE_DIR, filename)
	
	try:
		os.remove(file_path)
		return {"status ": "success ", " message": f"Deleted {filename}"}
	except FileNotFoundError:
		return FileNotFoundError
	except Exception as e:
		return {"error ":str(e)}

#-------------------| CSRF |-------------------|
# mockup db
users = {"admin": {"password": "1234", "email": "admin@example.com"},
         "asd": {"password": "asd123", "email": "asd@example.com"}}

# aktiv session-ok
sessions = {}

SESSION_COOKIE = "session_id"

#---------------post (login) endpoint---------------
# session cookie-ban tarolva
# input:
# output:
@app.post("/login/")
async def login(response: Response, username: str = Form(...), password: str = Form(...)):
    print(users[username]["password"] == password)
    if username in users and users[username]["password"] == password:
        session_id = secrets.token_hex(16)
        sessions[session_id] = username
        print(users)
        print(sessions)
        response.set_cookie(SESSION_COOKIE, session_id, httponly=True)
        return {"status": "success", "message": "Logged in"}
    
    return {"error": "Invalid credentials"}

# helper function az update-email endpoint-hoz
# csak kikeresi a jelenleg aktiv session-ok kozul a request-et kuldo cookie-jat
def get_current_user(request: Request):
    session_id = request.cookies.get(SESSION_COOKIE)
    if session_id and session_id in sessions:
        print(users)
        print(sessions)
        return sessions[session_id]
    return None

# email megvaltozatasa a jelenleg bejelentkezett felhasznalonak ->
# -> cookie-ban tarolt sessID alapajan
@app.post("/update-email/")
async def update_email(
    request: Request, new_email: str = Form(...)
):
    username = get_current_user(request)
    if username and username in users:
        users[username]["email"] = new_email
        print(users)
        print(sessions)
        return {"status": "success", "message": f"Email updated to {new_email}"}
    return {"error": "Unauthorized"}