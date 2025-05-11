from fastapi import FastAPI, Depends, Path
from typing import Annotated
from models.blogs import blogs 

app = FastAPI()

def blog_dependency(id: Annotated[int, Path(...)]):
    return blogs.get(id, "Blog not found")

@app.get("/blog/{id}")
def get_blog(blog_name: Annotated[str, Depends(blog_dependency)]):
    return {"blog": blog_name}
