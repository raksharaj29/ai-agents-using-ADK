from google.adk.agents import Agent


from ..tools.financial_tools import (
    calculate_savings,
    calculate_sip,
    save_income,
    save_expenses
)

financial_agent = Agent(
    name="financial_agent",
    model="gemini-2.5-flash",
    description="Handles financial calculations like savings and SIP.",
    instruction="""
    You are a Financial Agent.

    Help users with:
    - Monthly savings calculation
    - SIP calculations
    - Income and expense based calculations

    Use the available financial tools whenever calculation is required.
    """,
    tools=[
        calculate_savings,
        calculate_sip
    ],
)