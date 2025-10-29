import itertools
import re

def truth_table(expr, variables) -> str:
    """
    Generate a truth table for a digital logic expression.
    Operators:
      + = OR
      * = AND
      ! = NOT (postfix, e.g. A! or (A+B)!)
      ~ = XOR
    Example:
        print(truth_table("A*!B + (C*D)!", ["A", "B", "C", "D"]))
    """
    s = expr.replace(" ", "")

    # --- Handle postfix NOT for variables (A!) ---
    s = re.sub(r"([A-Za-z0-9_]+)!", r"(not \1)", s)

    # --- Handle postfix NOT for parentheses ((A+B)!) ---
    # repeat until no more matches
    while re.search(r"\([^()]+\)!", s):
        s = re.sub(r"(\([^()]+\))!", r"(not \1)", s)

    # --- XOR (~) → ^
    s = s.replace("~", "^")

    # --- AND (*) → and
    s = s.replace("*", " and ")

    # --- OR (+) → or
    s = s.replace("+", " or ")

    py_expr = s

    header = "  ".join(variables) + "  |  " + expr
    lines = [header, "-" * len(header)]

    for combo in itertools.product([0, 1], repeat=len(variables)):
        env = {var: bool(val) for var, val in zip(variables, combo)}

        try:
            result = eval(py_expr, {"__builtins__": None}, env)
            result_bit = int(bool(result))
        except Exception as e:
            result_bit = f"Error: {e}"

        values = "  ".join(str(v) for v in combo)
        lines.append(f"{values}  |  {result_bit}")

    return "\n".join(lines)
