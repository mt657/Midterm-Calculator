import pkg_resources
import logging

class OperationManager:
    """Manages dynamic loading of calculator operations."""
    
    def __init__(self):
        # Load operations during initialization
        self.operations = self.load_operations()
    
    def load_operations(self):
        """Loads available operations using entry points."""
        operations = {}
        for entry_point in pkg_resources.iter_entry_points(group='calculator.operations'):
            operation_name = entry_point.name
            operation_class = entry_point.load()  # Dynamically loads the operation class
            operations[operation_name] = operation_class
        logging.info(f"Operations loaded: {list(operations.keys())}")  # Log available operations
        return operations

    def get_operation(self, operation_name):
        """Fetches the operation class by name."""
        operation = self.operations.get(operation_name)
        if operation is None:
            logging.error(f"Operation '{operation_name}' not found.")  # Log missing operation
        return operation

    def list_operations(self):
        """Lists all available operations."""
        return list(self.operations.keys())
