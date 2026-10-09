import json
import sys
from pathlib import Path


DATA_FILE = Path("todos.json")


def load_todos():
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError

        return data

    except json.JSONDecodeError:
        print("Erro: o arquivo todos.json está inválido.")
        sys.exit(1)


def save_todos(todos):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(todos, file, ensure_ascii=False, indent=2)


def add_todo(text):
    todos = load_todos()

    next_id = max((todo["id"] for todo in todos), default=0) + 1

    todo = {
        "id": next_id,
        "text": text,
        "done": False
    }

    todos.append(todo)
    save_todos(todos)

    print(f"Tarefa criada: {next_id} - {text}")


def list_todos():
    todos = load_todos()

    if not todos:
        print("Nenhuma tarefa cadastrada.")
        return

    for todo in todos:
        status = "x" if todo["done"] else " "
        print(f'[{status}] {todo["id"]}: {todo["text"]}')


def edit_todo(todo_id, new_text):
    todos = load_todos()

    for todo in todos:
        if todo["id"] == todo_id:
            old_text = todo["text"]
            todo["text"] = new_text
            save_todos(todos)

            print(
                f'Tarefa {todo_id} atualizada: '
                f'"{old_text}" -> "{new_text}"'
            )
            return

    print(f"Erro: tarefa com ID {todo_id} não encontrada.")
    sys.exit(1)


def done_todo(todo_id):
    todos = load_todos()

    for todo in todos:
        if todo["id"] == todo_id:
            todo["done"] = True
            save_todos(todos)

            print(f"Tarefa {todo_id} concluída.")
            return

    print(f"Erro: tarefa com ID {todo_id} não encontrada.")
    sys.exit(1)


def remove_todo(todo_id):
    todos = load_todos()

    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            save_todos(todos)

            print(f"Tarefa {todo_id} removida.")
            return

    print(f"Erro: tarefa com ID {todo_id} não encontrada.")
    sys.exit(1)


def parse_id(value):
    try:
        return int(value)
    except ValueError:
        print("Erro: o ID precisa ser um número inteiro.")
        sys.exit(1)


def print_help():
    print("""
Uso:

  python todo.py add "texto da tarefa"
  python todo.py list
  python todo.py edit ID "novo texto"
  python todo.py done ID
  python todo.py rm ID
""")


def main():
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) != 3:
            print('Erro: use: python todo.py add "texto da tarefa"')
            sys.exit(1)

        add_todo(sys.argv[2])

    elif command == "list":
        if len(sys.argv) != 2:
            print("Erro: use: python todo.py list")
            sys.exit(1)

        list_todos()

    elif command == "edit":
        if len(sys.argv) != 4:
            print('Erro: use: python todo.py edit ID "novo texto"')
            sys.exit(1)

        todo_id = parse_id(sys.argv[2])
        new_text = sys.argv[3].strip()

        if not new_text:
            print("Erro: o novo texto não pode estar vazio.")
            sys.exit(1)

        edit_todo(todo_id, new_text)

    elif command == "done":
        if len(sys.argv) != 3:
            print("Erro: use: python todo.py done ID")
            sys.exit(1)

        done_todo(parse_id(sys.argv[2]))

    elif command == "rm":
        if len(sys.argv) != 3:
            print("Erro: use: python todo.py rm ID")
            sys.exit(1)

        remove_todo(parse_id(sys.argv[2]))

    else:
        print(f"Erro: comando desconhecido: {command}")
        print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()