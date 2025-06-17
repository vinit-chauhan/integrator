from langchain.tools import tool

from langchain.document_loaders import WebBaseLoader


@tool
def fetch_page(url: str) -> str:
    """Returns a text of the given web page"""

    loader = WebBaseLoader(web_path=url)
    res = ''
    for doc in loader.load():
        res += doc.page_content

    return res
