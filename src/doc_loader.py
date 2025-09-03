"""
doc_loader.py
-------------
Loads reference documents (pricing, services, FAQs, policies)
into memory for retrieval.

Functions to implement:
- load_docs() -> List[str]
    Loads documents from local files or directory and returns them as text.
"""

import os


def load_docs(data_dir: str = "data") -> list[dict]:
    """
    Loads all .txt documents from the given directory.

    Args:
        data_dir (str): Path to folder containing text documents.

    Returns:
        list[dict]: A list of dictionaries with 'filename' and 'content'
    """
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    data_dir = os.path.join(project_root, "data")

    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"Data directory not found: {data_dir}")

    docs = []
    for filename in os.listdir(data_dir):
        if filename.endswith(".txt"):
            filepath = os.path.join(data_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                docs.append({"filename": filename, "content": content})
    return docs

