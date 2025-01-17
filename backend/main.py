from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory list to store posts (for demonstration)
posts = []

class Post(BaseModel):
    content: str

@app.get("/posts")
def get_posts():
    return posts

@app.post("/posts")
def create_post(post: Post):
    posts.append(post.dict())
    return {"message": "Post created"}
