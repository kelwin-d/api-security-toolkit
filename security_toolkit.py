from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from pydantic import BaseModel, EmailStr
from collections import defaultdict

app = FastAPI()

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

rate_limit_store = defaultdict(list)
MAX_REQUESTS = 5
RATE_LIMIT_WINDOW = 60

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=403, detail="Invalid token")

@app.middleware("http")
async def rate_limiter(request: Request, call_next):
    client_ip = request.client.host
    current_time = datetime.utcnow().timestamp()

    rate_limit_store[client_ip] = [
        timestamp for timestamp in rate_limit_store[client_ip]
        if current_time - timestamp < RATE_LIMIT_WINDOW
    ]

    if len(rate_limit_store[client_ip]) >= MAX_REQUESTS:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    rate_limit_store[client_ip].append(current_time)
    return await call_next(request)

class InputData(BaseModel):
    email: EmailStr

@app.get("/secure-data")
async def secure_data(user: dict = Depends(verify_token)):
    return {"data": "Confidential Information"}

@app.post("/submit")
async def submit(data: InputData):
    return {"success": True, "message": "Data received successfully"}

@app.post("/token")
async def generate_token():
    return {"token": create_token({"sub": "user@example.com"})}

