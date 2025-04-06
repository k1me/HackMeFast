from fastapi import FastAPI, Form, Request, Response
from fastapi.responses import PlainTextResponse
import os, secrets, sqlite3
from fastapi.middleware.cors import CORSMiddleware

SESSION_COOKIE = "session_id"
BASE_DIR = "backend/static/example"
DB_PATH= "backend/users.db"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/read-file/")
async def read_file(filename: str):
    file_path = os.path.join(BASE_DIR, filename)
    
    try:
        with open(file_path, "r") as f:
            return PlainTextResponse(f.read())
    except FileNotFoundError:
        return {"error ": "File not found"}

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

@app.post("/login/")
async def login(response: Response, username: str = Form(...), password: str = Form(...)):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"Executing query: {query}")
    
    cursor.execute(query)
    user = cursor.fetchone()
    print(f"SQL result: {user}")
    
    if user:
        session_id = secrets.token_hex(16)
        query = cursor.execute("INSERT OR REPLACE INTO sessions (session_id, username) VALUES (?, ?)", (session_id, username))
        
        conn.commit()
        conn.close()

        response.set_cookie(SESSION_COOKIE, session_id, httponly=True)
        return {"status": "success", "message": "Logged in"}
    
    conn.close()
    return {"error": "Invalid credentials"}

def get_current_user(request: Request):
    session_id = request.cookies.get(SESSION_COOKIE)
    if not session_id:
        return None

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT username FROM sessions WHERE session_id = ?", (session_id,))
    user = cursor.fetchone()
    conn.close()

    return user[0] if user else None

@app.post("/update-password/")
async def update_email(request: Request, new_password: str = Form(...)):
    username = get_current_user(request)
    
    if username:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET password = ? WHERE username = ?", (new_password, username))
        conn.commit()
        conn.close()

        return {"status": "success", "message": f"Password updated to {new_password}"}
    
    return {"error": "Unauthorized"}