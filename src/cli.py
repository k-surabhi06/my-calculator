import sys
import click
from src.calculator import add, subtract, multiply, divide, power, square_root


@click.command()
@click.argument("operation")
@click.argument("numbers", type=float, nargs=-1)
def calculate(operation, numbers):
    """Simple calculator CLI"""

    # Handle missing operands gracefully
    if len(numbers) == 0:
        click.echo("Error: No operands provided")
        sys.exit(1)
    elif len(numbers) == 1:
        if operation in ["add", "subtract", "multiply", "divide", "power"]:
            click.echo(f"Error: {operation.capitalize()} requires 2 operands")
            sys.exit(1)
        num1 = numbers[0]
        num2 = None
    else:
        num1, num2 = numbers[0], numbers[1]

    try:
        # Perform the requested operation
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        elif operation == "power":
            result = power(num1, num2)
        elif operation == "square_root":
            result = square_root(num1)  # only 1 operand needed
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        # Format result for consistency
        if operation == "divide":
            result = round(result, 2)

        if isinstance(result, float) and result.is_integer():
            result = int(result)

        click.echo(result)

    except ValueError as e:
        click.echo(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        click.echo(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    calculate()

