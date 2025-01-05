from phi.agent import Agent
from phi.tools.apify import ApifyTools
from phi.model.groq import Groq

agent = Agent(
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[ApifyTools(api_key="apify_api_yj6RqFWoX4oUJ33R509TFC8aEnSs7D1ii0Cw",web_scraper=True)], 
    show_tool_calls=True
)
agent.print_response("Get the selectors of all important attributes like product name, id, description etc from the url https://www.dermstore.com/p/skinceuticals-c-e-ferulic-with-15-l-ascorbic-acid-vitamin-c-serum-30ml/11289609/", markdown=True)