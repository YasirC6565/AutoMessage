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

# from doc_loader import load_docs
# from simple_retriever import retrieve
#
#
# def main():
#     docs = load_docs()
#     query = "What services do you offer"
#     results = retrieve(query, docs, top_k=1)
#
#     print("Retriever Results:")
#     for r in results:
#         print(f"File: {r['filename']}")
#         print(f"Content: {r['content']}")
#         print("----")
#
#
# if __name__ == "__main__":
#     main()

# from input_cleaner import clean_text
from doc_loader import load_docs
from simple_retriever import retrieve
from tool_router import route_tool
from tools import execute_tool



def main():
    # 1. Simulated incoming enquiry
    query = "What services do you offer"

    # 2. Clean the query
    #cleaned_query = clean_text(query)

    # 3. Load reference documents
    docs = load_docs()

    # 4. Retrieve relevant document(s)
    results = retrieve(query, docs, top_k=1)

    print("Retriever Results:")
    for r in results:
        print(f"File: {r['filename']}")
        print(f"Content: {r['content']}")
        print("----")

    tool = route_tool(query)  # → "pricing"
    reply = execute_tool(tool, item="Item X")  # → calls pricing.run
    print(reply)

if __name__ == "__main__":
    main()

