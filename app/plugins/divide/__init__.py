from app.commands import Command
from app.plugins.operations import Operations

class DivideCommand(Command):

    def execute(self):
        a = int(input("Enter a:"))
        b = int(input("Enter b:"))
        print("Result:", Operations.divide(a,b))
        