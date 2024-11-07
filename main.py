# main.py

from app.calculator import Calculator

def center_text(text, width=50):
    """Center the text within a specified width.

    Args:
        text (str): The text to be centered.
        width (int): The width within which the text will be centered.

    Returns:
        str: The centered text.
    """
    return text.center(width)

def main():
    """Main interactive loop for the calculator.

    This function handles user input, executes calculator commands,
    and displays results or error messages to the user.
    """
    calculator = Calculator()

    print("\n" + "=" * 50)
    print(center_text("Welcome to the Interactive Calculator!", 50))
    print("=" * 50 + "\n")
    print(center_text("Type 'help' for a list of commands.", 50) + "\n")

    while True:
        user_input = input(">>> Enter command: ").strip()

        if user_input.lower() in ['exit', 'quit']:
            print("\n" + "=" * 50)
            print(center_text("Exiting the calculator. Goodbye!", 50))
            print("=" * 50 + "\n")
            break

        parts = user_input.split()
        command = parts[0]

        try:
            args = list(map(float, parts[1:]))  # Convert arguments to float
            output = calculator.execute_command(command, *args)

            # Determine if output is a numeric result, string message, or list (e.g., history)
            if isinstance(output, (int, float)):  # For numeric results
                print("\n" + "=" * 50)
                print()  # Add spacing above the result
                print(center_text(f"Result: {output}", 50))
                print()  # Add spacing below the result
                print("=" * 50 + "\n")  # Bottom border
            elif isinstance(output, list):  # For list results (e.g., history)
                print("\n" + "=" * 50)
                for line in output:
                    print(center_text(str(line), 50))  # Print each history item centered
                print("=" * 50 + "\n")
            else:  # For error/help messages as strings
                print("\n" + "=" * 50)
                print(center_text(output, 50))  # Center the error or message text
                print("=" * 50 + "\n")

        except ValueError:
            print("\n" + "=" * 50)
            print(center_text("Error: Invalid input.", 50))
            print(center_text("Please ensure you provide numbers as arguments.", 50))
            print("=" * 50 + "\n")

if __name__ == "__main__":  # pragma: no cover
    main()
