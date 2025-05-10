# FastAPI Pydantic Example

This project demonstrates how to use **FastAPI** with **Pydantic** for request validation and structured data models.

## Features
- FastAPI setup with Uvicorn server
- Pydantic models for validation
- Basic `/chat` POST endpoint

## How to Run

1. Create and activate virtual environment:
uv venv
source .venv/bin/activate # For Windows: .venv\Scripts\activate

2. Install dependencies:
uv add "fastapi[standard]"

3. Run the server:
uvicorn main:app --reload

4. Open in browser:
http://127.0.0.1:8000/docs

---

✅ Made with FastAPI & Pydantic  
👩‍💻 By Nirma