# Regras de negócio do todo sem depender do Typer
from datetime import datetime

from . import storage


def add(text: str) -> dict:
    data = storage.load()
    next_id = max((t["id"] for t in data["todos"]), default=0) + 1
    item = {
        "id": next_id,
        "text": text,
        "done": False,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }
    data["todos"].append(item)
    storage.save(data)
    return item


def list_items(show_done: bool = False) -> list:
    todos = storage.load()["todos"]
    return todos if show_done else [t for t in todos if not t["done"]]


def complete(todo_id: int) -> dict:
    data = storage.load()
    for item in data["todos"]:
        if item["id"] == todo_id:
            item["done"] = True
            storage.save(data)
            return item
    raise KeyError(todo_id)


def remove(todo_id: int) -> dict:
    data = storage.load()
    for i, item in enumerate(data["todos"]):
        if item["id"] == todo_id:
            removed = data["todos"].pop(i)
            storage.save(data)
            return removed
    raise KeyError(todo_id)
