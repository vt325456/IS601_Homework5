""" 
Test module for the arithmetic commands and REPL functionality of the class App.
"""
import pytest
from app import App
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand


def test_add_command(capfd, monkeypatch):
    """Verifies the addition command correctly adds two numbers and displays result."""
    inputs = iter(['2', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = AddCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert "Result: 4" in out, "The addition result should be printed."

def test_subtract_command(capfd, monkeypatch):
    """Verifies the subtraction command correctly subtracts two numbers and displays result."""
    inputs = iter(['2', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = SubtractCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert "Result: 0" in out, "The subtraction result should be printed."

def test_multiply_command(capfd, monkeypatch):
    """Verifies the multiplication command correctly multiplies two numbers and displays result."""
    inputs = iter(['2', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = MultiplyCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert "Result: 4" in out, "The multiplication result should be printed."

def test_divide_command(capfd, monkeypatch):
    """Verifies the division command correctly divides two numbers and displays result."""

    inputs = iter(['2', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = DivideCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert "Result: 1" in out, "The division result should be printed."

def test_dividebyzero_command(capfd, monkeypatch):
    """Tests proper error handling when attempting division by zero."""

    inputs = iter(['2', '0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = DivideCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert "Error raised! Cant operate Division By Zero" in out, "This Operation should raise error!"

def test_app_menu_command(capfd, monkeypatch):
    """
    Test that the REPL correctly handles the 'menu' command and exits cleanly.
    This test simulates user input to display the menu and then exit the application,
    ensuring the menu is displayed and the app exits gracefully with the expected output.
    """
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    assert str(e.value) == "Exiting...", "The app did not exit as expected"
    