from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/user/{username}/{id}")
def news(username: Annotated[str, Path(min_length=5, max_length=20, description = "Enter username")]
         , id: int = Path(ge=18, le= 120, description = "Enter age")) -> dict:
    return {"message": f"Hello, {username} {id}"}
# Enter User ID'