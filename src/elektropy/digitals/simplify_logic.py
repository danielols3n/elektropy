import re
import sympy as sp
from sympy.logic.boolalg import simplify_logic as sp_simplify_logic, And, Or, Not, Xor, BooleanTrue, BooleanFalse

_VAR_RE = r"[A-Za-z_]\w*"

def _infer_variables(expr: str):
    toks = set(re.findall(rf"\b{_VAR_RE}\b", expr))
    return sorted(toks)


def digital_to_sympy(expr: str, variables=None):
    """
    Convert digital notation to a SymPy boolean expression.
    Operators:
      * = AND
      + = OR
      ! = NOT (postfix, e.g. A! or (A+B)!)
      ~ = XOR (infix)
    """
    s = expr.replace(" ", "")

    # --- Handle postfix NOT for variables (A!) ---
    s = re.sub(rf"({_VAR_RE})!", r"~(\1)", s)

    # --- Handle postfix NOT for parentheses ((A+B)!) ---
    # repeat until no more matches
    while re.search(r"\([^()]+\)!", s):
        s = re.sub(r"(\([^()]+\))!", r"~\1", s)

    # --- Handle XOR (~) ---
    # Only replace XOR (~) when used between variables/expressions
    s = re.sub(r"(?<=\w)~(?=\w|\()", "^", s)

    # --- AND / OR ---
    s = s.replace("*", "&").replace("+", "|")

    # --- Constants ---
    s = re.sub(r"\b0\b", "False", s)
    s = re.sub(r"\b1\b", "True", s)

    # Prepare boolean symbols
    if variables is None:
        variables = _infer_variables(expr)
    symmap = {name: sp.symbols(name, boolean=True) for name in variables}

    # --- Sympify safely ---
    sympy_expr = sp.sympify(s, locals=symmap, evaluate=True)
    return sympy_expr


def sympy_to_digital(e) -> str:
    """Render a SymPy boolean expression back to postfix-! digital syntax."""
    if e is BooleanTrue:
        return "1"
    if e is BooleanFalse:
        return "0"
    if isinstance(e, sp.Symbol):
        return e.name
    if isinstance(e, Not):
        arg = list(e.args)[0]
        inner = sympy_to_digital(arg)
        # postfix NOT: A! or (expr)!
        if isinstance(arg, sp.Symbol):
            return inner + "!"
        else:
            return f"({inner})!"
    if isinstance(e, And):
        parts = [sympy_to_digital(a) for a in e.args]
        return "*".join(_maybe_paren(a, for_op="AND") for a in parts)
    if isinstance(e, Or):
        parts = [sympy_to_digital(a) for a in e.args]
        return "+".join(_maybe_paren(a, for_op="OR") for a in parts)
    if isinstance(e, Xor):
        parts = [sympy_to_digital(a) for a in e.args]
        return "~".join(_maybe_paren(a, for_op="XOR") for a in parts)
    return str(e)


def _maybe_paren(s: str, for_op: str) -> str:
    has_plus = "+" in s
    has_tilde = "~" in s
    has_star = "*" in s
    if for_op == "AND":
        if has_plus or has_tilde:
            return f"({s})"
    elif for_op == "XOR":
        if has_plus:
            return f"({s})"
    elif for_op == "OR":
        return s
    return s


def simplify_logic(expr: str, *, form: str = "auto", return_sympy: bool = False, variables=None):
    """
    Simplify Boolean expression in digital notation.
    Operators: * (AND), + (OR), ! (NOT postfix), ~ (XOR)
    """
    e = digital_to_sympy(expr, variables=variables)

    if form in ("dnf", "cnf"):
        es = sp_simplify_logic(e, form=form)
    else:
        es = sp_simplify_logic(e)

    return es if return_sympy else sympy_to_digital(es)
