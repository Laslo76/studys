from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    age: int


app = FastAPI()
users = []


@app.get("/users")
async def get_users():
    return 'ffff'


@app.post('/user/{username}/{age}')
async def add_user(username: str, age: int) -> User:
    user = User()
    try:
        user.id = users[-1].id + 1
    except IndexError:
        user.id = 1
    user.username = username
    user.age = age
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> str:
    try:
        edit_user = users[user_id]
        edit_user.username = username
        edit_user.age = age
        return edit_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def update_user(user_id: int) -> User:
    try:
        del_user = users.pop(user_id)
        return del_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
