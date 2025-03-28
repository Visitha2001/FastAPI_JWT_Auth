from fastapi import FastAPI , Depends , HTTPException , status
from fastapi.middleware.cors import CORSMiddleware

from routes.auth import router as auth_router
from routes.entry import entry_root
from routes.blog import blog_router

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*" , "http://localhost:5173/*" , "http://localhost:5173/blogs"],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include your routers
app.include_router(auth_router)
app.include_router(entry_root)
app.include_router(blog_router)