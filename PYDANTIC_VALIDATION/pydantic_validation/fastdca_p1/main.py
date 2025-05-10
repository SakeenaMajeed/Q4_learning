from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from uuid import uuid4
from typing import List, Dict

app = FastAPI()

chat_history: Dict[str, List[dict]] = {}


class Metadata(BaseModel):
    model: str
    temperature: float = 0.7
    top_p: float = 0.9

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    user_id: str
    metadata: Metadata
    messages: List[Message]

class ChatResponseMetadata(BaseModel):
    timestamp: str
    session_id: str

class ChatResponse(BaseModel):
    user_id: str
    reply: str
    metadata: ChatResponseMetadata

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    if not request.messages:
        raise HTTPException(status_code=400, detail="Messages list cannot be empty")

    last_message = request.messages[-1].content

    if request.user_id not in chat_history:
        chat_history[request.user_id] = []

    chat_history[request.user_id].append({
        "role": "user",
        "content": last_message,
        "timestamp": datetime.utcnow().isoformat()
    })

    reply = f"Hello, how are you ladybug?"

    chat_history[request.user_id].append({
        "role": "bot",
        "content": reply,
        "timestamp": datetime.utcnow().isoformat()
    })

    return {
        "user_id": request.user_id,
        "reply": reply,
        "metadata": {
            "timestamp": datetime.utcnow().isoformat(),
            "session_id": str(uuid4())
        }
    }