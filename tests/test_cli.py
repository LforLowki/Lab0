import pytest
from click.testing import CliRunner
from src.cli import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_remove_missing_cli(runner):
    result = runner.invoke(cli, ["clean", "remove-missing", "1", "", "2"])
    assert "1" in result.output
    assert "2" in result.output

def test_fill_missing_cli(runner):
    result = runner.invoke(cli, ["clean", "fill-missing", "1", "", "2", "--fill", "5"])
    assert "5" in result.output

def test_normalize_cli(runner):
    result = runner.invoke(cli, ["numeric", "normalize", "1", "2", "3"])
    assert result.exit_code == 0

def test_tokenize_cli(runner):
    result = runner.invoke(cli, ["text", "tokenize", "Hello World!"])
    assert "hello" in result.output

def test_shuffle_cli(runner):
    result = runner.invoke(cli, ["struct", "shuffle", "1", "2", "3", "--seed", "1"])
    assert result.exit_code == 0

