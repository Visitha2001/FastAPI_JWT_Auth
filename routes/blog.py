from fastapi import APIRouter
from controllers.blog import create_blog, get_all_blogs, get_blog_by_id, update_blog_by_id, delete_blog_by_id
from models.blog import BlogModel

blog_router = APIRouter()

# Create a new blog
@blog_router.post("/new/blog")
async def new_blog(doc: BlogModel):
    return await create_blog(doc)

# Get all blogs
@blog_router.get("/all/blog")
async def all_blogs():
    return await get_all_blogs()

# Get a blog by ID
@blog_router.get("/blog/{_id}")
async def get_blog(_id: str):
    return await get_blog_by_id(_id)

# Update a blog by ID
@blog_router.patch("/update/{_id}")
async def update_blog(_id: str, doc: BlogModel):
    return await update_blog_by_id(_id, doc)

# Delete a blog by ID
@blog_router.delete("/delete/{_id}")
async def delete_blog(_id: str):
    return await delete_blog_by_id(_id)