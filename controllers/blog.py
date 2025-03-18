from bson import ObjectId
import datetime
from models.blog import BlogModel
from config.config import blogs_collection
from serializers.blog import DecodeBlog, DecodeBlogs

# Create a new blog
async def create_blog(doc: BlogModel):
    doc = dict(doc)
    current_date = datetime.date.today()
    doc["date"] = str(current_date)
    res = blogs_collection.insert_one(doc)
    doc_id = res.inserted_id
    return {
        "message": "Blog created successfully",
        "blog_id": str(doc_id)
    }

# Get all blogs
async def get_all_blogs():
    res = blogs_collection.find()
    decoded_data = DecodeBlogs(res)
    return {
        "status": "ok",
        "data": decoded_data
    }

# Get a single blog by ID
async def get_blog_by_id(_id: str):
    res = blogs_collection.find_one({"_id": ObjectId(_id)})
    if res:
        decoded_data = DecodeBlog(res)
        return {
            "status": "ok",
            "data": decoded_data
        }
    else:
        return {
            "status": "error",
            "message": "Blog not found"
        }

# Update a blog by ID
async def update_blog_by_id(_id: str, doc: BlogModel):
    doc = dict(doc)
    res = blogs_collection.update_one({"_id": ObjectId(_id)}, {"$set": doc})
    if res.modified_count > 0:
        return {
            "status": "ok",
            "message": "Blog updated successfully"
        }
    else:
        return {
            "status": "error",
            "message": "Blog not found or no changes made"
        }

# Delete a blog by ID
async def delete_blog_by_id(_id: str):
    res = blogs_collection.delete_one({"_id": ObjectId(_id)})
    if res.deleted_count > 0:
        return {
            "status": "ok",
            "message": "Blog deleted successfully"
        }