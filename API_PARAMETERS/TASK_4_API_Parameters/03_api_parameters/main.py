from fastapi import FastAPI
from routes import batman

app = FastAPI(title="FastAPI Parameters Demo")

app.include_router(batman.router)
