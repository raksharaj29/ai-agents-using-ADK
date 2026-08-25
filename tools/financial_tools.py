from google.adk.tools.tool_context import ToolContext


def calculate_savings(
    income: float,
    expenses: float
) -> str:

    savings = income - expenses

    return f"Monthly savings: ₹{savings:.2f}"


def calculate_sip(
    monthly_investment: float,
    annual_return: float,
    years: int
) -> str:

    monthly_rate = annual_return / 100 / 12
    months = years * 12

    future_value = (
        monthly_investment
        * (((1 + monthly_rate) ** months - 1) / monthly_rate)
        * (1 + monthly_rate)
    )

    return f"Estimated value: ₹{future_value:.2f}"


def save_income(
    income: float,
    tool_context: ToolContext
) -> str:

    tool_context.state["income"] = income

    return f"Income ₹{income:.2f} saved."


def save_expenses(
    expenses: float,
    tool_context: ToolContext
) -> str:

    tool_context.state["expenses"] = expenses

    return f"Expenses ₹{expenses:.2f} saved."