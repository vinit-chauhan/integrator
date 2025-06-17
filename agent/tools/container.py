from langchain.tools import BaseTool


class ToolList():
    tool_list: list[BaseTool]

    def __init__(self, tool_list: list[BaseTool] = []) -> None:
        self.tool_list = tool_list

    def register(self, tool: BaseTool) -> None:
        self.tool_list.append(tool)

    def register_all(self, tools: list[BaseTool]) -> None:
        for tool in tools:
            self.tool_list.append(tool)

    def get_list(self) -> list[BaseTool]:
        return self.tool_list

    def __str__(self) -> str:
        res = 'tools=['

        for tool in self.tool_list:
            res += f'{tool.name}, '

        res += '\b\b]'

        return res
