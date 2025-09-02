"""
main.py
-------
Entry point for the MVP system.

Responsibilities:
- Accept an incoming message (simulated for now with a test string).
- Pass the message through the input cleaner.
- Load reference documents.
- Use the retriever to find relevant context.
- Route the enquiry to the correct tool.
- Generate a reply.
- Log each step for debugging.

Flow (MVP1):
1. Receive message input (e.g., hardcoded string for now).
2. Clean input using input_cleaner.clean_text().
3. Load docs via doc_loader.load_docs().
4. Retrieve relevant info with simple_retriever.retrieve().
5. Route to correct tool using tool_router.route_tool().
6. Execute tool (e.g., tools/pricing.get_price()).
7. Return or print the final reply.
"""


