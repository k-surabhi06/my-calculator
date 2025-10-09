import sys
import click
from calculator import add, subtract, multiply, divide, power, square_root

@click.command()
@click.argument('operation')
@click.argument('numbers', type=float, nargs=2)
def calculate(operation, numbers):
    """Simple calculator CLI"""
    try:
        if operation == 'add':
            result = add(numbers[0], numbers[1])
        elif operation == 'subtract':
            result = subtract(numbers[0], numbers[1])
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        if result == int(result):
            click.echo(int(result))
        else:
            click.echo(f"{result:.2f}")

    except Exception as e:
        click.echo(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    calculate()
