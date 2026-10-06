"""Persistência simples em JSON.

O arquivo fica em ~/.prodcli/data.json, ou no caminho definido
pela variável de ambiente PRODCLI_HOME (útil para testes).
"""
import json
import os
from pathlib import Path


def data_path() -> Path:
    home = Path(os.environ.get("PRODCLI_HOME", Path.home() / ".prodcli"))
    home.mkdir(parents=True, exist_ok=True)
    return home / "data.json"


def load() -> dict:
    path = data_path()
    if not path.exists():
        return {"todos": []}
    return json.loads(path.read_text(encoding="utf-8"))


def save(data: dict) -> None:
    data_path().write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )
