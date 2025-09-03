"""
simple_retriever.py
-------------------
Retrieves relevant document snippets based on a query (user enquiry).

Functions to implement:
- retrieve(query: str, docs: List[str]) -> List[str]
    Returns a list of the most relevant document snippets.
"""

import re


def retrieve(query: str, docs: list[dict], top_k: int = 1) -> list[dict]:
    """
    Retrieves the most relevant documents based on keyword overlap.
    """
    # Split query into lowercase words
    query_words = set(re.findall(r"\w+", query.lower()))

    scored_docs = []
    for doc in docs:
        content_words = set(re.findall(r"\w+", doc["content"].lower()))
        # Score = number of overlapping words
        score = len(query_words & content_words)
        scored_docs.append((score, doc))

    # Sort by score (descending)
    scored_docs.sort(key=lambda x: x[0], reverse=True)

    # Return top_k docs (filtering out score=0)
    results = [doc for score, doc in scored_docs if score > 0]
    return results[:top_k]
