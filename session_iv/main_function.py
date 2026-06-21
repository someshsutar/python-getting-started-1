# ==========================================
# Demonstrating the Main Function in Python
# ==========================================

def add(a, b):
    """Adds two numbers"""
    return a + b


def multiply(a, b):
    """Multiplies two numbers"""
    return a * b


def display_welcome():
    print("Welcome to Python Main Function Demo")


def main():
    """
    Application entry point
    """

    display_welcome()

    num1 = 10
    num2 = 20

    total = add(num1, num2)
    product = multiply(num1, num2)

    print(f"\nNumbers: {num1}, {num2}")
    print(f"Addition      : {total}")
    print(f"Multiplication: {product}")

    print("\nApplication Completed")


# Program Entry Point
if __name__ == "__main__":
    main()