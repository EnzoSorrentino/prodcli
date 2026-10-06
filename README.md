# prodcli

CLI de produtividade no terminal, feita com Python e [Typer](https://typer.tiangolo.com/).
Os comandos crescem aos poucos: `todo` (pronto), `notes`, `timer` e `habit` (roadmap).

## Instalação

```bash
git clone <url-do-repo>
cd prodcli
pip install -e ".[dev]"
```

## Uso

```bash
prod todo add "estudar FastAPI"
prod todo list
prod todo done 1
prod todo list --all
prod todo rm 1
prod --version
```

Os dados ficam em `~/.prodcli/data.json` (ou em `$PRODCLI_HOME`).

## Testes

```bash
pytest
```

## Roadmap

- [x] `todo` (add, list, done, rm)
- [ ] `notes`
- [ ] `timer` (pomodoro)
- [ ] `habit` (com streak)

## Licença

MIT
