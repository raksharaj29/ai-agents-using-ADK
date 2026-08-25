from google.adk.agents import Agent

from .financial_agent.agent import financial_agent
from .expense_agent.agent import expense_agent


root_agent = Agent(
    name="ai_agent_pro",
    model="gemini-2.5-flash",
    description="Main financial assistant with financial and expense agents.",
    instruction="""
    You are the main assistant.

    You have two specialist agents:

    1. Financial Agent
    - Savings calculation
    - SIP calculation
    - Income related calculations

    2. Expense Agent
    - Expense tracking
    - Adding expenses
    - Total expense calculation

    Ask the user which agent they want to use:

    1. Financial Agent
    2. Expense Agent

    If the user chooses Financial Agent, transfer the task to Financial Agent.

    If the user chooses Expense Agent, transfer the task to Expense Agent.
    """,
    sub_agents=[
        financial_agent,
        expense_agent
    ],
)