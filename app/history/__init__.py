import pandas as pd
import os
from typing import List
from app.calculation import Calculation
from app.operations.addition import Addition
from app.operations.subtraction import Subtraction
from app.operations.multiplication import Multiplication
from app.operations.division import Division

# Global operation map to map operation names to the corresponding operation objects
operation_map = {
    "Addition": Addition(),
    "Subtraction": Subtraction(),
    "Multiplication": Multiplication(),
    "Division": Division()
}

class History:
    """Class to keep track of calculation history with undo, clear, save, and load functionality."""

    def __init__(self):
        """Initialize an empty list to store calculation history and ensure the history file exists."""
        self._history: List[Calculation] = []
        self.filename = "history.csv"  # Hardcode the filename
        
        # Create the history file if it doesn't exist
        if not os.path.exists(self.filename):
            # Create an empty DataFrame and save it as a CSV file to initialize the file
            pd.DataFrame(columns=["operand1", "operation", "operand2", "result"]).to_csv(self.filename, index=False)

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

    def save(self) -> str:
        """
        Save the history to a CSV file.

        Returns:
            str: Confirmation message that history has been saved.
        """
        # Convert the list of Calculation objects to a DataFrame
        history_data = [{
            "operand1": calc.operand1,
            "operation": calc.operation.__class__.__name__,
            "operand2": calc.operand2,
            "result": calc.result
        } for calc in self._history]

        # Create DataFrame and save to CSV
        df = pd.DataFrame(history_data)
        df.to_csv(self.filename, index=False)  # Save to the hardcoded filename
        return f"History saved to {self.filename}."

    def load(self) -> str:
        """
        Load the history from the hardcoded 'history.csv' file
        and add each calculation to the Calculator's history.

        Returns:
            str: Message indicating the result of the load operation.
        """
        if not os.path.exists(self.filename):
            return f"Error: {self.filename} not found."

        try:
            df = pd.read_csv(self.filename)

            if df.empty:
                return f"Error: {self.filename} is empty or corrupted."

            self._history.clear()

            for _, row in df.iterrows():
                operand1 = float(row["operand1"])
                operation_name = row["operation"]
                operand2 = float(row["operand2"])
                result = float(row["result"])

                operation = operation_map.get(operation_name, None)

                if operation:
                    calculation = Calculation(operation, operand1, operand2)
                    calculation.set_result(result)
                    self.add_calculation(calculation)
                else:
                    print(f"Error: Operation {operation_name} not recognized.")

        except pd.errors.EmptyDataError:
            return f"Error: {self.filename} is empty or corrupted."
        except Exception as e:
            return f"Error: {str(e)}"

        return f"History loaded from {self.filename}."

    def get_history(self) -> List[Calculation]:
        """
        Retrieve the entire calculation history.

        Returns:
            List[Calculation]: The history list of calculations.
        """
        return self._history
