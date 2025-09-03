def run(*args, **kwargs) -> str:
    date = kwargs.get("date", "unspecified date")
    return f"[Scheduler Tool] Initialising... (date={date})"
