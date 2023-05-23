from os import environ
from fastapi import FastAPI, HTTPException
from pyairtable import Table
from pydantic import BaseModel


auth_token = environ['auth_token']
base_id = environ['base_id']
table_name = environ['table_name']

app = FastAPI()

table = Table(auth_token, base_id, table_name)

class Maigck(BaseModel):
    email: str
    name: str

class UserCreate(BaseModel):
    Name: str
    Email: str
    Status: str
    Maigck: Maigck

def get_record_or_404(id: str) -> dict:
    record = table.get(id)
    if record:
        return record
    raise HTTPException(status_code=404, detail="User not found")

# Example request - http://localhost:5000/users - with method GET
@app.get('/users', tags=["Users"])
def get_users():
    users = [fields for fields in table.iterate(page_size=50, max_records=150)]
    return {"users": users}


# Example request - http://localhost:5000/users/2 - with method GET
@app.get('/users/{id}', tags=["Users"])
def get_user(id: str) -> dict:
    record = get_record_or_404(id)
    return {"user": record}


# Example request - http://localhost:5000/users/ - with method POST
@app.post('/users', tags=["Users"])
def add_user(user: UserCreate):
    record = table.batch_create([user.dict()])
    return {"user": record}


# Example request - http://localhost:5000/users/2 - with method PUT
@app.put('/users/{id}', tags=["Users"])
def update_user(id: str, user: UserCreate):
    updated_fields = user.dict()
    record = table.update(id, updated_fields)
    if record:
        return {"user": record}
    raise HTTPException(status_code=404, detail="User not found")


# Example request - http://localhost:5000/users/2 - with method DELETE
@app.delete('/users/{id}', tags=["Users"])
def remove_user(id: str) -> dict:
    deleted = table.delete(id)
    if deleted:
        return {"id": id, "deleted": deleted}
    raise HTTPException(status_code=404, detail="User not found")