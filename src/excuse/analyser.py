"""Module responsible for excuse analysis."""


def analyze(excuse: str) -> dict:
    """Analyze the given excuse and return some metrics.

    This is a stub implementation; replace with real logic.
    """
    return {"length": len(excuse), "has_please": "please" in excuse.lower()}
