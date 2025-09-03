from src.tools import pricing, schedular

# Registry maps tool name → function
TOOL_REGISTRY = {
    "pricing": pricing.run,
    "scheduler": schedular.run,
}

def execute_tool(tool_name: str, *args, **kwargs) -> str:
    """
    Executes the tool function from the registry.

    Args:
        tool_name (str): Name of the tool (e.g., 'pricing', 'scheduler').
        *args, **kwargs: Passed directly to the tool function.

    Returns:
        str: Tool output or error message.
    """
    tool_func = TOOL_REGISTRY.get(tool_name)
    if tool_func:
        return tool_func(*args, **kwargs)
    return f"Error: Tool '{tool_name}' not found."
