from pydantic import BaseModel

class BlogModel(BaseModel):
    title: str
    subtitle: str
    content: str
    author: str
    tags: list
