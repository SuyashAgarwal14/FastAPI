from fastapi import APIRouter, HTTPException, Header, Depends
from datetime import datetime
import random
from models import LoginRequest, LoginResponse, PromptRequest, PromptResponse, HistoryItem
from auth import authenticate_user, create_token, get_user_from_token
from history import load_history, save_history


router = APIRouter()
HISTORY_FILE = load_history()

DUMMY_RESPONSES = [
    "Interesting... Let's explore that idea.",
    "Let me think about it...",
    "That's a great question!",
    "Here's something to consider.",
    "Can you tell me more?",
    "I'm not sure, but let's find out together.",
    "Why did the Python programmer wear glasses? Because he couldn't C!",
    "That's fascinating!",
    "Let me get back to you on that.",
    "I appreciate your curiosity!"
]

def get_current_user(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format")
    token = authorization.split(" ")[1]
    user = get_user_from_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return user

@router.post("/login/", response_model=LoginResponse)
def login(req: LoginRequest):
    if not authenticate_user(req.username, req.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_token(req.username)
    return {"token": token}

@router.post("/prompt/", response_model=PromptResponse)
def submit_prompt(req: PromptRequest, user: str = Depends(get_current_user)):
    response = random.choice(DUMMY_RESPONSES)
    entry = {
        "timestamp": datetime.utcnow().isoformat(timespec="seconds"),
        "prompt": req.prompt,
        "response": response
    }
    HISTORY_FILE.setdefault(user, []).append(entry)
    save_history(HISTORY_FILE)
    return {"response": response}

@router.get("/history/", response_model=list[HistoryItem])
def get_history(user: str = Depends(get_current_user)):
    return HISTORY_FILE.get(user, [])
