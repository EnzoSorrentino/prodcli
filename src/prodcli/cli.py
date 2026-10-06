import typer

from . import __version__, todo

app = typer.Typer(help="CLI de produtividade no terminal.", no_args_is_help=True)
todo_app = typer.Typer(help="Gerencie suas tarefas.", no_args_is_help=True)
app.add_typer(todo_app, name="todo")


def _version(value: bool):
    if value:
        typer.echo(f"prodcli {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        False, "--version", callback=_version, is_eager=True, help="Mostra a versão."
    ),
):
    pass


@todo_app.command("add")
def todo_add(text: str = typer.Argument(..., help="Texto da tarefa.")):
    """Adiciona uma tarefa."""
    item = todo.add(text)
    typer.echo(f"Tarefa #{item['id']} adicionada: {item['text']}")


@todo_app.command("list")
def todo_list(
    all_: bool = typer.Option(False, "--all", "-a", help="Inclui tarefas concluídas.")
):
    """Lista as tarefas pendentes."""
    items = todo.list_items(show_done=all_)
    if not items:
        typer.echo("Nenhuma tarefa por aqui.")
        return
    for t in items:
        mark = "x" if t["done"] else " "
        typer.echo(f"[{mark}] {t['id']:>3}  {t['text']}")


@todo_app.command("done")
def todo_done(todo_id: int = typer.Argument(..., help="ID da tarefa.")):
    """Marca uma tarefa como concluída."""
    try:
        item = todo.complete(todo_id)
    except KeyError:
        typer.echo(f"Tarefa #{todo_id} não encontrada.", err=True)
        raise typer.Exit(code=1)
    typer.echo(f"Tarefa #{item['id']} concluída.")


@todo_app.command("rm")
def todo_rm(todo_id: int = typer.Argument(..., help="ID da tarefa.")):
    """Remove uma tarefa."""
    try:
        item = todo.remove(todo_id)
    except KeyError:
        typer.echo(f"Tarefa #{todo_id} não encontrada.", err=True)
        raise typer.Exit(code=1)
    typer.echo(f"Tarefa #{item['id']} removida.")


if __name__ == "__main__":
    app()
