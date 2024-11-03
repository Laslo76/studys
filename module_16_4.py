from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


def find_user(find_id: int, ind=0):
    for i in range(ind, len(users)):
        if users[i].id == find_id:
            return i
    raise IndexError


@app.get("/users")
async def get_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def add_user(username: str, age: int, user: User) -> User:
    try:
        user_id = users[-1].id + 1
    except IndexError:
        user_id = 1
    user.id = user_id
    user.username = username
    user.age = age
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> User:
    try:
        edit_user = users[find_user(user_id)]
        edit_user.username = username
        edit_user.age = age
        return edit_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> User:
    try:
        index_users = find_user(user_id)
        del_user = users.pop(index_users)
        return del_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
