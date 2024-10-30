from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


class User(BaseModel):
    id: int
    username: str
    age: int


users = list()

app = FastAPI()


def find_user(find_id: int, users: User, ret_index=False) -> User:
    ind = 0
    for us in users:
        if us.id == find_id:
            if ret_index:
                return ind
            else:
                return us
        ind += 1
    raise IndexError


@app.get("/users")
async def get_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def add_user(user: User) -> User:
    try:
        user.id = users[-1].id + 1
    except IndexError:
        user.id = 1
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> User:
    try:
        edit_user = find_user(user_id, users)
        edit_user.username = username
        edit_user.age = age
        return edit_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> User:
    try:
        index_users = find_user(user_id, users, True)
        del_user = users.pop(index_users)
        return del_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
