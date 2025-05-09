from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from uuid import uuid4
from typing import List, Optional

app = FastAPI(
    title="DACA Chatbot API",
    description="A FastAPI-powered API designed for a chatbot featured in the DACA tutorial series.",
    version="0.1.0",
)

# Metadata Model
class Metadata(BaseModel):
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    session_id: str = Field(default_factory=lambda: str(uuid4()))

# Message Model
class Message(BaseModel):
    user_id: str
    text: str
    metadata: Metadata
    tags: Optional[List[str]] = None

# Response Model
class Response(BaseModel):
    user_id: str
    reply: str
    metadata: Metadata

# In-memory data store (for demo purposes)
users_data = {}

# Home Route
@app.get("/")
async def root():
    return {"message": "Welcome to the DACA Chatbot API! Access /docs for the API documentation."}

# Get User Route
@app.get("/users/{user_id}")
async def get_user(user_id: str, role: Optional[str] = None):
    if user_id in users_data:
        return {"user_id": user_id, "role": role if role else "guest"}
    raise HTTPException(status_code=404, detail="User not found")

# Get all users Route
@app.get("/users/")
async def get_all_users():
    if not users_data:
        raise HTTPException(status_code=404, detail="No users found")
    return users_data

# Chat Route
@app.post("/chat/", response_model=Response)
async def chat(message: Message):
    if not message.text.strip():
        raise HTTPException(status_code=400, detail="Message text cannot be empty")

    reply_text = f"Hello, {message.user_id}! You said: '{message.text}'. How can I assist you today?"
    # Save message for demo purposes
    users_data[message.user_id] = {"text": message.text, "metadata": message.metadata}
    return Response(
        user_id=message.user_id,
        reply=reply_text,
        metadata=Metadata()
    )

# Update Message Route
@app.put("/chat/{user_id}")
async def update_message(user_id: str, message: Message):
    if user_id not in users_data:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Update the message text and metadata for the user
    users_data[user_id] = {"text": message.text, "metadata": message.metadata}
    return {"message": "Message updated successfully"}

# Delete Message Route
@app.delete("/chat/{user_id}")
async def delete_message(user_id: str):
    if user_id not in users_data:
        raise HTTPException(status_code=404, detail="User not found")
    
    del users_data[user_id]
    return {"message": "Message deleted successfully"}

# Health Check Route
@app.get("/health")
async def health_check():
    return {"status": "API is up and running!"}




