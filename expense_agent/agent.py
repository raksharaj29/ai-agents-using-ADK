from google.adk.agents import Agent
from ..tools.expense_tools import calculate_expense

expense_agent = Agent(
    name="expense_agent",
    model="gemini-2.5-flash",
    description="Handles expense tracking and expense calculations.",
    instruction="""
    You are an Expense Agent.

    Help users with:
    - Adding expenses
    - Calculating total expenses
    - Tracking spending
    - Updating remaining money

    Use the expense tools whenever required.
    """,
    tools=[
        calculate_expense
    ],
)