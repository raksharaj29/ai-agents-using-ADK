from google.adk.agents import Agent

from .financial_agent.agent import financial_agent
from .expense_agent.agent import expense_agent
from .budget_agent.agent import budget_agent


root_agent = Agent(
    name="ai_agent_pro",
    model="gemini-2.5-flash",

    description="A financial assistant with multiple specialized agents.",

    instruction="""
    You are the main financial assistant.

    Route the user's request to the appropriate specialized agent.

    Use:
    - Financial Agent for savings and SIP calculations
    - Expense Agent for expense-related requests
    - Budget Agent for budgeting and budget planning

    Choose the appropriate agent based on the user's request.
    """,

    sub_agents=[
        financial_agent,
        expense_agent,
        budget_agent
    ],
)