import json
from typing import List
from app.calculation import Calculation

class History:
    """Class to keep track of calculation history with undo, clear, save, and load functionality."""

    def __init__(self):
        """Initialize an empty list to store calculation history."""
        self._history: List[Calculation] = []

    def add_calculation(self, calculation: Calculation):
        """
        Add a Calculation object to the history.

        Args:
            calculation (Calculation): A Calculation object to add to history.
        """
        self._history.append(calculation)

    def undo(self) -> str:
        """
        Undo the last calculation.

        Returns:
            str: Information about the undone calculation or a message if no history is present.
        """
        if not self._history:
            return "No history to undo."

        last_calculation = self._history.pop()
        return f"Undone: {last_calculation}"

    def clear(self) -> str:
        """
        Clear the entire history of calculations.

        Returns:
            str: Confirmation message that history has been cleared.
        """
        self._history.clear()
        return "History cleared."

    def save(self, filename: str = "history.json") -> str:
        """
        Save the history to a JSON file.

        Args:
            filename (str): The name of the file to save the history to. Defaults to 'history.json'.

        Returns:
            str: Confirmation message that history has been saved.
        """
        with open(filename, "w") as file:
            json.dump([calc.__dict__ for calc in self._history], file)
        return f"History saved to {filename}."

    def load(self, filename: str = "history.json") -> str:
        """
        Load the history from a JSON file.

        Args:
            filename (str): The name of the file to load the history from. Defaults to 'history.json'.

        Returns:
            str: Confirmation message that history has been loaded or error message if file not found.
        """
        try:
            with open(filename, "r") as file:
                self._history = [Calculation(**entry) for entry in json.load(file)]
            return f"History loaded from {filename}."
        except FileNotFoundError:
            return f"Error: {filename} not found."
        except json.JSONDecodeError:
            return f"Error: Failed to decode history data from {filename}."

    def get_history(self) -> List[Calculation]:
        """
        Retrieve the entire calculation history.

        Returns:
            List[Calculation]: The history list of calculations.
        """
        return self._history
