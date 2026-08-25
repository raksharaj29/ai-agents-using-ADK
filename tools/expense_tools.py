def calculate_expense(
    current_expenses: float,
    new_expense: float
) -> dict:
    """
    Calculate updated total expenses.

    Args:
        current_expenses: Current total expenses.
        new_expense: New expense amount.

    Returns:
        Updated expense information.
    """

    total_expenses = current_expenses + new_expense

    return {
        "current_expenses": current_expenses,
        "new_expense": new_expense,
        "total_expenses": total_expenses
    }