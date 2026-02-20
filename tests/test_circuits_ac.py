import sympy as sp

from elektropy import mesh_current_ac, node_voltage_ac


def _parse_complex_value(value: str, unit: str) -> complex:
    numeric = value.replace(unit, "").replace(" ", "")
    return complex(numeric)


def test_node_voltage_ac_complex():
    V1, V2 = sp.symbols("V1 V2")
    equations = [sp.Eq(V1 + V2, 3 - 1j), sp.Eq(V1 - V2, 1 + 3j)]

    result = node_voltage_ac(equations, ["V1", "V2"])
    v1 = _parse_complex_value(result["V1"], "V")
    v2 = _parse_complex_value(result["V2"], "V")

    assert abs(v1 - (2 + 1j)) < 1e-5
    assert abs(v2 - (1 - 2j)) < 1e-5


def test_mesh_current_ac_complex():
    I1, I2 = sp.symbols("I1 I2")
    equations = [
        sp.Eq((1 + 1j) * I1 + I2, 1 + 2j),
        sp.Eq(I1 + (2 - 1j) * I2, 4 - 2j),
    ]

    result = mesh_current_ac(equations, ["I1", "I2"])
    i1 = _parse_complex_value(result["I1"], "A")
    i2 = _parse_complex_value(result["I2"], "A")

    assert abs(i1 - (1 + 2j)) < 1e-5
    assert abs(i2 - (2 - 1j)) < 1e-5
