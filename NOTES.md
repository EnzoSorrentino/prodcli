# Notas do projeto (contexto entre sessões)

## Decisões
- Python + Typer; comandos agrupados em sub-apps (`prod todo ...`).
- Armazenamento em JSON único: `~/.prodcli/data.json`, sobrescrevível com `PRODCLI_HOME` (os testes usam isso).
- Regra de negócio fica em módulos próprios (`todo.py`), separada da camada CLI (`cli.py`).
- Novo comando = novo módulo + novo sub-app em `cli.py` + testes em `tests/`.
- Chave nova no JSON precisa de default em `storage.load()`.

## Padrão para cada comando novo
1. Criar `src/prodcli/<comando>.py` com a lógica.
2. Registrar o sub-app em `cli.py`.
3. Testes em `tests/test_<comando>.py` usando `CliRunner` e `PRODCLI_HOME` temporário.
4. Marcar no roadmap do README.

## Próximos passos
- `todo edit` e prioridades
- `notes add/list/search`
- `timer` (pomodoro)
- `habit` com streak

## Verificação
`python -m pytest -q`
