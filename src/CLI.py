import sys
import click
from calculator import add, subtract, multiply, divide, power, square_root

@click.command()
@click.argument("operation")
@click.argument("numbers", type=float, nargs=-1)
def calculate(operation, numbers):
    """Simple calculator CLI"""
    try:
        if len(numbers) < 2 and operation != "square_root":
            sys.exit("Please provide at least two numbers.")

        num1, num2 = numbers[0], numbers[1] if len(numbers) > 1 else (numbers[0], None)

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
            result = square_root(num1)
        else:
            sys.exit()

        print(result)

    except Exception:
        sys.exit()

if __name__ == "__main__":
    calculate()
