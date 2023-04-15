import json

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(description="Service for managing TODOs")
with open("openapi.json", "w") as fh:
    json.dump(obj=app.openapi(), fp=fh)

# A simple in-memory database to store our todos
db = []


# Define a Todo model using Pydantic BaseModel
class Todo(BaseModel):
    title: str
    description: str = None
    completed: bool = False


# Create a new todo
@app.post("/todos/")
def create_todo(todo: Todo):
    db.append(todo)
    return {"message": "Todo created successfully"}


# Get all todos
@app.get("/todos/")
def get_todos():
    return db


# Get a single todo by id
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    return db[todo_id]


# Update a todo
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: Todo):
    db[todo_id] = todo
    return {"message": "Todo updated successfully"}


# Delete a todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    db.pop(todo_id)
    return {"message": "Todo deleted successfully"}
