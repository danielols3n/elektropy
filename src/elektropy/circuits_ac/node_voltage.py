import sympy as sp


def _parse_symbols(variables):
    symbols = sp.symbols(" ".join(variables))
    if isinstance(symbols, sp.Symbol):
        return (symbols,)
    return tuple(symbols)


def _format_complex_value(value, decimals: int, unit: str) -> str:
    z = complex(sp.N(value, decimals + 2))
    real = round(z.real, decimals)
    imag = round(z.imag, decimals)

    tol = 10 ** (-decimals)
    if abs(real) < tol:
        real = 0.0
    if abs(imag) < tol:
        imag = 0.0

    if imag == 0:
        return f"{real} {unit}"
    if real == 0:
        return f"{imag}j {unit}"

    sign = "+" if imag >= 0 else "-"
    return f"{real} {sign} {abs(imag)}j {unit}"


def node_voltage(equations, variables, decimals=5) -> dict:
    """
    Solve a system of equations using the Node Voltage Method with complex values.

    Arguments:
    equations (list): A list of sympy equations representing the circuit.
    variables (list): A list of symbols (as strings) representing node voltages.
    decimals (int): Number of decimals in the formatted output.

    Returns:
    dict: Mapping of variable name to formatted voltage value with unit (V).
    """
    symbols = _parse_symbols(variables)
    expressions = [sp.sympify(eq) for eq in equations]
    solutions_list = sp.solve(expressions, symbols, dict=True)

    if not solutions_list:
        raise ValueError("No solution found for the given equations.")

    solution = solutions_list[0]
    return {str(var): _format_complex_value(solution[var], decimals, "V") for var in symbols}
