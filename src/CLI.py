import sys
import click
from calculator import add, subtract, multiply, divide, power, square_root


@click.command()
@click.argument("operation")
@click.argument("numbers", type=float, nargs=-1)
def calculate(operation, numbers):
    """Simple calculator CLI"""
    try:
        if operation == "add":
            if len(numbers) != 2:
                click.echo(f"Unexpected error: add requires exactly 2 numbers")
                sys.exit(1)
            result = add(numbers[0], numbers[1])
        elif operation == "subtract":
            if len(numbers) != 2:
                click.echo(f"Unexpected error: subtract requires exactly 2 numbers")
                sys.exit(1)
            result = subtract(numbers[0], numbers[1])
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)
        if operation == "add": 
            result = add(num1, num2) 
        elif operation == "subtract": 
            result = subtract(num1, num2) 
        elif operation == "multiply": 
            result = multiply(num1, num2) 
        elif operation == "divide": 
            result = divide(num1, num2) 
        else:
            click.echo(f"Unknown operation: {operation}") 
            sys.exit(1) 
        

        # Format result nicely
        if result == int(result):
            click.echo(int(result))
        else:
            click.echo(f"{result:.2f}")

    except Exception as e:
        click.echo(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    calculate()
