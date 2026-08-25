# Financial Expense Agent

A multi-agent financial assistant built using Google Agent Development Kit (ADK) and Gemini.

## Agents

### Financial Agent

Handles:

- Monthly savings calculation
- SIP calculations
- Income and expense calculations

### Expense Agent

Handles:

- Expense tracking
- Expense calculations
- Spending-related queries

## Architecture

User
↓
Root Agent
↓
LLM
↓
Financial Agent / Expense Agent
↓
Tools
↓
Tool Result
↓
LLM
↓
Final Response

## Tech Stack

- Python
- Google ADK
- Gemini
- UV
- Google Generative AI
