import logging
import pandas as pd
import os
from typing import List
from app.calculation import Calculation
from app.operations.addition import Addition
from app.operations.subtraction import Subtraction
from app.operations.multiplication import Multiplication
from app.operations.division import Division

# Initialize the logger for this module
logger = logging.getLogger(__name__)

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
            pd.DataFrame(columns=["operand1", "operation", "operand2", "result"]).to_csv(self.filename, index=False)
            logger.info(f"History file {self.filename} created.")

    def add_calculation(self, calculation: Calculation):
        """
        Add a Calculation object to the history.

        Args:
            calculation (Calculation): A Calculation object to add to history.
        """
        self._history.append(calculation)
        logger.info(f"Added calculation to history: {calculation}")

    def undo(self) -> str:
        """
        Undo the last calculation.

        Returns:
            str: Information about the undone calculation or a message if no history is present.
        """
        if not self._history:
            logger.warning("Attempted to undo with no history.")
            return "No history to undo."

        last_calculation = self._history.pop()
        logger.info(f"Undone calculation: {last_calculation}")
        return f"Undone: {last_calculation}"

    def clear(self) -> str:
        """
        Clear the entire history of calculations.

        Returns:
            str: Confirmation message that history has been cleared.
        """
        self._history.clear()
        logger.info("Cleared calculation history.")
        return "History cleared."

    def save(self) -> str:
        """
        Save the history to a CSV file.

        Returns:
            str: Confirmation message that history has been saved.
        """
        history_data = [{
            "operand1": calc.operand1,
            "operation": calc.operation.__class__.__name__,
            "operand2": calc.operand2,
            "result": calc.result
        } for calc in self._history]

        df = pd.DataFrame(history_data)
        df.to_csv(self.filename, index=False)
        logger.info(f"History saved to {self.filename}.")
        return f"History saved to {self.filename}."

    def load(self) -> str:
        """
        Load the history from the hardcoded 'history.csv' file
        and add each calculation to the Calculator's history.

        Returns:
            str: Message indicating the result of the load operation.
        """
        if not os.path.exists(self.filename):
            logger.error(f"File {self.filename} not found during load operation.")
            return f"Error: {self.filename} not found."

        try:
            df = pd.read_csv(self.filename)

            # Check if the file is empty
            if df.empty:
                logger.error(f"{self.filename} is empty or corrupted.")
                return f"Error: {self.filename} is empty or corrupted."

            # Clear existing history before loading the new one
            self._history.clear()

            for _, row in df.iterrows():
                try:
                    operand1 = float(row["operand1"])
                    operation_name = row["operation"]
                    operand2 = float(row["operand2"])
                    result = float(row["result"])

                    operation = operation_map.get(operation_name, None)

                    if operation:
                        calculation = Calculation(operation, operand1, operand2)
                        calculation.set_result(result)
                        self.add_calculation(calculation)
                        logger.info(f"Loaded calculation: {calculation}")
                    else:
                        logger.error(f"Operation {operation_name} not recognized during load.")
                        return f"Error: Operation {operation_name} not recognized."

                except ValueError as e:
                    logger.error(f"Error processing row: {e}")
                    return f"Error: Invalid data in {self.filename}."

        except pd.errors.EmptyDataError:
            logger.error(f"{self.filename} is empty or corrupted.")
            return f"Error: {self.filename} is empty or corrupted."
        except Exception as e:
            logger.error(f"An error occurred while loading history: {str(e)}")
            return f"Error: {str(e)}"

        logger.info(f"History loaded from {self.filename}.")
        return f"History loaded from {self.filename}."

    def get_history(self) -> List[Calculation]:
        """
        Retrieve the entire calculation history.

        Returns:
            List[Calculation]: The history list of calculations.
        """
        logger.info("Retrieving calculation history.")
        return self._history
