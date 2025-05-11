from fastapi import HTTPException, status
from ..models.blogs import blogs

class GetObjectOr404:
    def __init__(self, model: dict) -> None:
        self.model = model

    def __call__(self, id: str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Object ID {id} not found")
        return obj

blog_dependency = GetObjectOr404(blogs)
