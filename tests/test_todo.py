import pytest
from typer.testing import CliRunner

from prodcli.cli import app

runner = CliRunner()


@pytest.fixture(autouse=True)
def isolated_home(tmp_path, monkeypatch):
    monkeypatch.setenv("PRODCLI_HOME", str(tmp_path))


def test_add_and_list():
    result = runner.invoke(app, ["todo", "add", "estudar FastAPI"])
    assert result.exit_code == 0
    assert "#1" in result.output

    result = runner.invoke(app, ["todo", "list"])
    assert "estudar FastAPI" in result.output


def test_done_hides_from_default_list_but_shows_with_all():
    runner.invoke(app, ["todo", "add", "tarefa A"])
    runner.invoke(app, ["todo", "done", "1"])

    assert "tarefa A" not in runner.invoke(app, ["todo", "list"]).output
    assert "tarefa A" in runner.invoke(app, ["todo", "list", "--all"]).output


def test_new_id_is_max_existing_id_plus_one():
    runner.invoke(app, ["todo", "add", "um"])
    runner.invoke(app, ["todo", "add", "dois"])
    runner.invoke(app, ["todo", "rm", "2"])
    result = runner.invoke(app, ["todo", "add", "três"])
    assert "#2" in result.output  # maior id restante (1) + 1


def test_unknown_id_returns_error():
    result = runner.invoke(app, ["todo", "done", "99"])
    assert result.exit_code == 1


def test_version():
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "0.1.0" in result.output
