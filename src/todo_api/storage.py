from datetime import datetime
from typing import Dict, List, Optional

from .models import TodoCreate, TodoResponse


class InMemoryStorage:
    def __init__(self):
        self._todos: Dict[int, dict] = {}
        self._next_id: int = 1

    def create(self, todo: TodoCreate) -> TodoResponse:
        todo_id = self._next_id
        self._next_id += 1

        now = datetime.now()
        todo_dict = {
            "id": todo_id,
            "title": todo.title,
            "description": todo.description,
            "completed": todo.completed,
            "created_at": now,
            "updated_at": now,
        }
        self._todos[todo_id] = todo_dict
        return TodoResponse(**todo_dict)

    def get_all(self) -> List[TodoResponse]:
        return [TodoResponse(**todo) for todo in self._todos.values()]

    def get_by_id(self, todo_id: int) -> Optional[TodoResponse]:
        todo = self._todos.get(todo_id)
        if todo:
            return TodoResponse(**todo)
        return None

    def clear(self) -> None:
        """Clear all todos - useful for testing"""
        self._todos.clear()
        self._next_id = 1


# Global storage instance
storage = InMemoryStorage()
