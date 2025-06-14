from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import os

app = FastAPI()

DATABASE = "knowledge_base.db"

class QueryRequest(BaseModel):
    question: str

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/")
def root():
    return {"message": "Welcome to the TDS Virtual TA API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/query")
def query_knowledge_base(request: QueryRequest):
    question = request.question
    # Placeholder for actual semantic search logic
    # For now, just return the question received
    return {"answer": f"Received question: {question}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
