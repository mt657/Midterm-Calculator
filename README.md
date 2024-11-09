# Interactive Calculator

This interactive calculator supports basic arithmetic operations (addition, subtraction, multiplication, division, modulus, and power) and includes features like history tracking and logging. The application uses various design patterns to ensure clean architecture and maintainability.

## Features

- **Basic operations**: Addition, subtraction, multiplication, division, modulus, and power.
- **History tracking**: Keeps track of all calculations and can display them on demand.
- **Logging**: Logs calculator sessions and errors for debugging and tracking purposes.
- **Environment variable support**: Customizes behavior through environment variables.

---

## Design Patterns

In this project, several design patterns are implemented to ensure a scalable and maintainable calculator application. These patterns include:

1. **Singleton Pattern**: Ensures that only one instance of the calculator exists. This is implemented in the `SingletonCalculator` class, which ensures that each calculator command uses the same instance throughout the application's lifecycle.

   **Link to implementation**: [SingletonCalculator Class](app/calculator/calculator_singleton.py)

2. **Strategy Pattern**: Used for the different mathematical operations (e.g., addition, subtraction, multiplication, division). Each operation is encapsulated in its own class, and the `Calculator` class delegates the operation selection to these strategy classes.

   **Link to implementation**: [Operation Strategy](app/operations/)

3. **Observer Pattern**: Used to maintain the history of calculations and notify observers (e.g., `HistoryObserver`) whenever a new calculation is performed. This pattern allows the history to be updated without tightly coupling the `Calculator` class to the history functionality.

   **Link to implementation**: [History Observer](app/history/history.py)

---

## Environment Variables

Environment variables are used to configure certain aspects of the application, such as the log file and the history file. This allows the user to customize the application's behavior without modifying the codebase.

The configuration values are read from the `.env` file using the `dotenv` library. These variables are used for logging and storing calculation history.

- **LOG_FILE**: Specifies the name of the log file where all application logs will be stored.
- **HISTORY_FILENAME**: Specifies the name of the CSV file where calculation history is saved.

### Code example to read environment variables:

```python
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

LOG_FILE = os.getenv('LOG_FILE', 'calculator.log')
HISTORY_FILENAME = os.getenv('HISTORY_FILENAME', 'history.csv')
```

**Link to implementation**: [Environment Variables Usage](main.py)

---

## Logging

The application uses logging to track events, errors, and other important activities. The logging configuration is set up in the `logger_config.py` file, which configures logging to a file and includes different logging levels (INFO, ERROR, etc.).

- **INFO level**: Used to track regular activities such as the start and end of calculator sessions.
- **ERROR level**: Used to log exceptions and invalid input.

This enables you to track user actions and application errors while keeping the logs centralized.

### Code example for logging setup:

```python
import logging
from logging.handlers import RotatingFileHandler

def setup_logging():
    """Set up the logging configuration."""
    logger = logging.getLogger()
    handler = RotatingFileHandler(LOG_FILE, maxBytes=5000000, backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
```

**Link to implementation**: [Logging Configuration](app/logger_config.py)

---

## Exception Handling (LBYL vs EAFP)

In this project, both **Look Before You Leap** (LBYL) and **Easier to Ask for Forgiveness than Permission** (EAFP) strategies are used for input validation and error handling.

1. **Look Before You Leap (LBYL)**: This approach checks whether the inputs are valid before attempting any calculations. For instance, before performing division or modulus operations, the program checks whether the denominator is zero.

    - **Code example (LBYL)**:  
    ```python
    if b == 0:
        raise ValueError("Cannot divide by zero")
    ```

    **Link to implementation**: [Division Class](app/operations/division.py)

2. **Easier to Ask for Forgiveness than Permission (EAFP)**: In this approach, the program attempts to execute the operation and handles exceptions (like invalid input or division by zero) when they occur. This is used in places where it is impractical to check every possible error beforehand.

    - **Code example (EAFP)**:  
    ```python
    try:
        result = calculator.execute_command(command, *args)
    except ValueError:
        print("Error: Invalid input")
    ```

    **Link to implementation**: [Main Program](main.py)

---

## Video Demonstration

A short video demonstration of the calculator, highlighting key features and functionalities, will showcase how to:

- Perform basic and advanced calculations.
- Use commands like `history`, `clear`, and `exit`.
- Handle errors and input validation.

**Link to video demonstration**: [Video Demonstration of Calculator](<insert_video_link_here>)

---

## Installation and Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/calculator.git
    cd calculator
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root of the project to set up environment variables:

    ```bash
    LOG_FILE=calculator.log
    HISTORY_FILENAME=history.csv
    ```

4. Run the calculator:

    ```bash
    python main.py
    ```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to replace `<insert_video_link_here>` with the actual link to your video when it's ready! Let me know if you'd like any further adjustments.