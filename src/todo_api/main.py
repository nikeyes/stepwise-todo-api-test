from typing import List

from fastapi import FastAPI, HTTPException, status

from .models import TodoCreate, TodoResponse
from .storage import storage

app = FastAPI(
    title="TODO API",
    description="Simple TODO API for stepwise plugin validation",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "TODO API",
        "docs": "/docs",
        "endpoints": {
            "implemented": ["GET /todos", "GET /todos/{id}", "POST /todos"],
            "not_implemented": [
                "PATCH /todos/{id}",
                "DELETE /todos/{id}",
                "GET /todos/search",
            ],
        },
    }


@app.get("/todos", response_model=List[TodoResponse])
def get_todos():
    """Get all todos"""
    return storage.get_all()


@app.get("/todos/search")
def search_todos(q: str = ""):
    """Search/filter todos - NOT IMPLEMENTED"""
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail=(
            "GET /todos/search is not implemented yet. "
            "This endpoint should search/filter todos by query."
        ),
    )


@app.get("/todos/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int):
    """Get a specific todo by ID"""
    todo = storage.get_by_id(todo_id)
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with id {todo_id} not found",
        )
    return todo


@app.post("/todos", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate):
    """Create a new todo"""
    return storage.create(todo)


# Stub endpoints - return 501 Not Implemented
@app.patch("/todos/{todo_id}")
def update_todo(todo_id: int):
    """Update a todo - NOT IMPLEMENTED"""
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="PATCH /todos/{id} is not implemented yet. This endpoint should update a todo.",
    )


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    """Delete a todo - NOT IMPLEMENTED"""
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="DELETE /todos/{id} is not implemented yet. This endpoint should delete a todo.",
    )
