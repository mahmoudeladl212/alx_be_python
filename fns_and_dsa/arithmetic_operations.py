def perform_operation(num1: float, num2: float, operation: str) -> float | str:
    """
    Perform basic arithmetic operations on two numbers.
    
    Args:
        num1: First operand
        num2: Second operand
        operation: One of 'add', 'subtract', 'multiply', or 'divide'
        
    Returns:
        Result of the arithmetic operation as float, or error message for division by zero
    """
    operation = operation.lower()  # Ensure case-insensitive comparison
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        return num1 / num2
    else:
        return "Error: Invalid operation"