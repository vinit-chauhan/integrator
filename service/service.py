from typing import Any
from prompts import generate_readme
from agent import agent
from langchain_core.output_parsers import StrOutputParser


def run() -> Any:

    _parser = StrOutputParser()

    document_url = 'https://www.cisco.com/site/us/en/products/security/identity-services-engine/index.html'

    prompt = generate_readme.prompt.invoke(
        {'document_url': document_url}).to_string()

    executor = agent.executor

    res = executor.invoke({'input': prompt})

    return res
