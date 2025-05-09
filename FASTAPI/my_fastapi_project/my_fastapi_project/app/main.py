from fastapi import FastAPI
from app.routes import batman

app = FastAPI()

# Include the Batman route
app.include_router(batman.router)
