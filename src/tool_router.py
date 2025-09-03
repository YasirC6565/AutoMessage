"""
tool_router.py
--------------
Routes an enquiry to the correct tool based on intent.

Functions to implement:
- route_tool(query: str) -> str
    Determines which tool should be executed for the given query.
"""

def route_tool(query: str) -> str:
    """
    Determines which tool should be executed for the given query.

    Args:
        query (str): The cleaned user enquiry.

    Returns:
        str: Tool name to use (must match registry key, e.g., 'pricing', 'scheduler').
    """
    query = query.lower()

    # Pricing-related
    pricing_keywords = ["price", "cost", "how much"]
    if any(word in query for word in pricing_keywords):
        return "pricing"

    # Scheduling-related
    scheduler_keywords = ["book", "schedule", "appointment", "reserve"]
    if any(word in query for word in scheduler_keywords):
        return "scheduler"

    # Default fallback
    return "unsupported"