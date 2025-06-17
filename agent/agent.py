import os
from agent.tools import tool_list

from dotenv import load_dotenv

from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI


load_dotenv()

agent_prompt = hub.pull('hwchase17/react')
agent_llm = ChatOpenAI(model=os.environ.get('OPENAI_MODEL', 'gpt-4o-mini'))


agent = create_react_agent(
    tools=tool_list.get_list(),
    prompt=agent_prompt,
    llm=agent_llm
)


executor = AgentExecutor(
    agent=agent,
    tools=tool_list.get_list(),
    verbose=True
)
