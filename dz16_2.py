from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
@app.get("/user/{user_id}")
def user_id(user_id: int = Path(ge=1, le= 100, description = "Enter User ID")) -> dict:
    return {"message": f"Hello, {user_id} "}

@app.get("/user/{username}/{age}")
def username_age(username: Annotated[str, Path(min_length=5, max_length=20, description = "Enter username")]
         , age: int = Path(ge=18, le= 120, description = "Enter age")) -> dict:
    return {"message": f"Hello, {username} {age}"}
