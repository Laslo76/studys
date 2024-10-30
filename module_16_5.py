from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory='templates')


class User(BaseModel):
    id: int
    username: str
    age: int


def find_user(find_id: int, users_list: User, ret_index=False) -> User:
    ind = 0
    for us in users_list:
        if us.id == find_id:
            if ret_index:
                return ind
            else:
                return us
        ind += 1
    raise IndexError

users = []

app = FastAPI()


@app.get("/")
async def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})



@app.get("/user/{user_id}")
async def get_users(user_id: int, request: Request) -> HTMLResponse:
    try:
        user = find_user(user_id, users)
        return templates.TemplateResponse("users.html", {"request": request, "user": user})
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.post('/user/{username}/{age}')
async def add_user(user: User, request: Request) -> HTMLResponse:
    try:
        user.id = users[-1].id + 1
    except IndexError:
        user.id = 1
    users.append(user)
    return templates.TemplateResponse("users.html", {"request": request, "user": user})


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int, request: Request) -> HTMLResponse:
    try:
        edit_user = find_user(user_id, users)
        edit_user.username = username
        edit_user.age = age
        return templates.TemplateResponse("users.html", {"request": request, "user": edit_user})
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int, request: Request) -> HTMLResponse:
    try:
        index_users = find_user(user_id, users, True)
        del_user = users.pop(index_users)
        return templates.TemplateResponse("users.html", {"request": request, "users": users})
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")