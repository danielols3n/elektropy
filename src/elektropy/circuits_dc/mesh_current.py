import sympy as sp

def mesh_current_dc(equations, variables, decimals = 5) -> dict:
    """
    Solve a system of equations using the Mesh Current Method.
    """

    """
    Arguments:
    equations (list): A list of sympy equations representing the circuit.
    variables (list): A list of sympy symbols representing the node voltages to solve for.
    decimals (int): Number of decimal places to round the results to.
    """
    
    """
    Returns: 
    A dictionary mapping variable names to their solved values in amperes, rounded to the specified number of decimal places.
    """
    symbols = sp.symbols(variables) 
    expressions = [sp.sympify(eq) for eq in equations]
    solutions = sp.solve(expressions, symbols)

    if not solutions: 
        raise ValueError("No solution found for the given equations.")
    
    result = {str(var): f"{round(float(solutions[var]), decimals)} A" for var in symbols}

    return result
