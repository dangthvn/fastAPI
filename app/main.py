from fastapi import FastAPI

from .routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# try:
#     conn = psycopg2.connect(host='localhost', database ='fastapi', user='postgres', password='admin', cursor_factory=RealDictCursor)
#     cursor = conn.cursor()
#     print("Database connection was successful!")
# except Exception as error:
#     print("Database connection failed!")
#     print("Error:", error)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router) 

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI Application!!!"} 