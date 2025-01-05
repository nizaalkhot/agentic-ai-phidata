from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

## web search agent
websearch_agent = Agent(
    name = "Web Search Agent",
    role = "Search the web for the information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools = [DuckDuckGo()],
    instructions = ["Always include sources"],
    show_tool_calls = True,
    markdown = True
)

## Financial agent
financial_agent = Agent(
    name = "Financial AI Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools = [
        YFinanceTools(stock_price=True,stock_fundamentals=True)
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent = Agent(
    team = [websearch_agent,financial_agent],
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    instructions = ["Always include sources","Use table to display the data"],
    show_tool_calls = True,
    markdown = True,
)

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for Tesla",stream=True)