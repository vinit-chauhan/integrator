from .container import ToolList
from .web_search import web_search_tool
from .fetch_page import fetch_page


tool_list = ToolList()


tool_list.register_all(
    [
        web_search_tool,
        fetch_page
    ]
)
