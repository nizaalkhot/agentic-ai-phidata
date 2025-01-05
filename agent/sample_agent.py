from phi.agent import Agent, RunResponse
from phi.model.groq import Groq

agent = Agent(
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    markdown=True
)

# Get the response in a variable
# run: RunResponse = agent.run("Share a 2 sentence horror story.")
# print(run.content)

# Print the response in the terminal
agent.print_response("How are you?")