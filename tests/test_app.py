'''
Unit tests for the App class's REPL (Read-Eval-Print Loop) behavior.
'''
from app import App

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    App.start()
    out, err = capfd.readouterr()

    assert "Calculator Program. Type 'exit' to exit." in out
    assert "Exiting..." in out

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, err = capfd.readouterr()

    assert "Calculator Program. Type 'exit' to exit." in out
    assert "Unknown command. Type 'exit' to exit." in out
    assert "Exiting..." in out
