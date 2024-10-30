from fastapi import FastAPI


app = FastAPI()
users = {'1': 'Имя: Example, Возраст: 18'}


@app.get("/users")
async def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def add_user(username: str, age: int) -> str:
    new_id = str(max(map(int, users.keys())) + 1)
    users[new_id] = f'Имя: {username}, Возраст:{age}'
    return f'User {new_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str, username: str, age: str) -> str:
    users[user_id] = f'Имя: {username}, Возраст:{age}'
    return f'The user {user_id} is registered'


@app.delete('/user/{user_id}')
async def update_user(user_id: str) -> str:
    users.pop(user_id)
    return f'The user {user_id} is deleted'

