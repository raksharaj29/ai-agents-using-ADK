def calculate_budget_balance(
    income: float,
    total_budget: float
) -> str:

    balance = income - total_budget

    return f"Remaining budget: ₹{balance:.2f}"


def calculate_category_budget(
    income: float,
    percentage: float
) -> str:

    amount = income * percentage / 100

    return f"Budget amount: ₹{amount:.2f}"


def check_budget_limit(
    budget_limit: float,
    actual_spending: float
) -> str:

    difference = budget_limit - actual_spending

    if difference >= 0:
        return f"Within budget. Remaining: ₹{difference:.2f}"

    return f"Budget exceeded by: ₹{abs(difference):.2f}"


def calculate_budget_percentage(
    income: float,
    amount: float
) -> str:

    percentage = (amount / income) * 100

    return f"{percentage:.2f}% of income"