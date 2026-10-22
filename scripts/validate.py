# Build: 6c9a3e59275ab1e31e2383ddea7f75ac

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
