from setuptools import setup, find_packages

setup(
    name="Midterm-Calculator",
    version="0.1.0",  # Define your version
    packages=find_packages(),  # Automatically find all packages (like app)
    entry_points={  # This is where the plugin system for operations is set up
        "calculator.operations": [  # Register operations under this group
            "addition = app.operations.addition:Addition",  # Register Addition class
            "subtraction = app.operations.subtraction:Subtraction",  # Subtraction class
            "multiplication = app.operations.multiplication:Multiplication",  # Multiplication class
            "division = app.operations.division:Division",  # Division class
            'modulus = app.operations.modulus:Modulus',  # New modulus operation
            'power = app.operations.power:Power',        # New power operation
            # Add new operations here as plugins:
            # "new_operation = app.operations.new_operation:NewOperation",  # Example for a new operation
        ],
    },
)

