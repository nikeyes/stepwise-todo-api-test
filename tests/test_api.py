import pytest
from fastapi.testclient import TestClient

from src.todo_api.main import app
from src.todo_api.storage import storage


@pytest.fixture(autouse=True)
def reset_storage():
    """Reset storage before each test"""
    storage.clear()
    yield
    storage.clear()


@pytest.fixture
def client():
    return TestClient(app)


def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "endpoints" in data


def test_get_todos_empty(client):
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == []


def test_create_todo(client):
    todo_data = {
        "title": "Test Todo",
        "description": "Test Description",
        "completed": False,
    }
    response = client.post("/todos", json=todo_data)
    assert response.status_code == 201

    data = response.json()
    assert data["title"] == "Test Todo"
    assert data["description"] == "Test Description"
    assert data["completed"] is False
    assert "id" in data
    assert "created_at" in data
    assert "updated_at" in data


def test_create_todo_minimal(client):
    todo_data = {"title": "Minimal Todo"}
    response = client.post("/todos", json=todo_data)
    assert response.status_code == 201

    data = response.json()
    assert data["title"] == "Minimal Todo"
    assert data["description"] is None
    assert data["completed"] is False


def test_create_todo_invalid_empty_title(client):
    todo_data = {"title": ""}
    response = client.post("/todos", json=todo_data)
    assert response.status_code == 422


def test_get_todos_after_creation(client):
    # Create two todos
    client.post("/todos", json={"title": "Todo 1"})
    client.post("/todos", json={"title": "Todo 2"})

    response = client.get("/todos")
    assert response.status_code == 200

    todos = response.json()
    assert len(todos) == 2
    assert todos[0]["title"] == "Todo 1"
    assert todos[1]["title"] == "Todo 2"


def test_get_todo_by_id(client):
    # Create a todo
    create_response = client.post("/todos", json={"title": "Test Todo"})
    todo_id = create_response.json()["id"]

    # Get it by ID
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == todo_id
    assert data["title"] == "Test Todo"


def test_get_todo_not_found(client):
    response = client.get("/todos/999")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()


def test_update_todo_not_implemented(client):
    response = client.patch("/todos/1", json={"completed": True})
    assert response.status_code == 501
    assert "not implemented" in response.json()["detail"].lower()


def test_delete_todo_not_implemented(client):
    response = client.delete("/todos/1")
    assert response.status_code == 501
    assert "not implemented" in response.json()["detail"].lower()


def test_search_todos_not_implemented(client):
    response = client.get("/todos/search?q=test")
    assert response.status_code == 501
    assert "not implemented" in response.json()["detail"].lower()
