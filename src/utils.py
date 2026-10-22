# Build: a8ffe86a3080d0afdaa0b514089132e1

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
