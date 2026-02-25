import sympy as sp

def series_resistance(*resistors) -> float:
    """
    Calculate the total resistance of resistors in series.
    """

    """
    Arguments: resitors (float or int)
    """
    return f"{sum(resistors)} Ω"

def parallell_resistance(*resistors) -> float:
    """
    Calculate the total resistance of resistors in parallel.
    """

    """
    Arguments: resitors (float or int)
    """

    reciprocal = sum(1 / r for r in resistors)
    return f"{1 / reciprocal} Ω" if reciprocal != 0 else float('inf')