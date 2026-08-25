from google.adk.agents import Agent

from ..tools.budget_tools import (
    calculate_budget_balance,
    calculate_category_budget,
    check_budget_limit,
    calculate_budget_percentage,
)


budget_agent = Agent(
    name="budget_agent",
    model="gemini-2.5-flash",

    description="Handles budgeting and budget-related calculations.",

    instruction="""
    You are a Budget Agent.

    Help users with:
    - Monthly budget planning
    - Category-wise budget allocation
    - Checking budget limits
    - Calculating budget percentages
    - Checking remaining budget

    Always use the available tools when a numerical
    calculation is required.
    """,

    tools=[
        calculate_budget_balance,
        calculate_category_budget,
        check_budget_limit,
        calculate_budget_percentage,
    ],
)