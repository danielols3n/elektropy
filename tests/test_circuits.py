import math
import pytest
from sympy import symbols, Eq

from elektropy import (
    series_resistance,
    parallell_resistance,
    node_voltage,
    mesh_current,
    power_vi,
    power_ri,
    power_rv,
    voltage_divider,
    current_divider,
    Thevenin,
    Norton,
    thevenin_from_voc_isc,
    norton_from_voc_isc,
)


def test_series_resistance():
    result = series_resistance(10, 20, 30)
    assert isinstance(result, str)
    assert "Ω" in result
    assert result.startswith("60")  # "60 Ω" or "60.0 Ω"


def test_parallell_resistance_two():
    result = parallell_resistance(10, 20)
    assert isinstance(result, str)
    assert "Ω" in result
    value = float(result.split()[0])
    assert pytest.approx(value, rel=1e-6) == 1 / (1 / 10 + 1 / 20)


def test_parallell_resistance_three_equal():
    result = parallell_resistance(5, 5, 5)
    assert isinstance(result, str)
    assert "Ω" in result
    value = float(result.split()[0])
    assert pytest.approx(value, rel=1e-6) == 1 / (1 / 5 + 1 / 5 + 1 / 5)


def test_node_voltage():
    V1, V2 = symbols("V1 V2")
    equations = [Eq(V1 + V2, 10), Eq(V1 - V2, 4)]
    variables = ["V1", "V2"]
    result = node_voltage(equations, variables)
    # If your function returns strings like {"V1": "7.0 V", "V2": "3.0 V"}
    v1 = float(result["V1"].split()[0]) if isinstance(result["V1"], str) else result["V1"]
    v2 = float(result["V2"].split()[0]) if isinstance(result["V2"], str) else result["V2"]
    assert round(v1, 6) == round(7.0, 6)
    assert round(v2, 6) == round(3.0, 6)


def test_mesh_current():
    I1, I2 = symbols("I1 I2")
    equations = [Eq(I1 + I2, 5), Eq(I1 - I2, 1)]
    variables = ["I1", "I2"]
    result = mesh_current(equations, variables)
    # If result contains "A"
    i1 = float(result["I1"].split()[0]) if isinstance(result["I1"], str) else result["I1"]
    i2 = float(result["I2"].split()[0]) if isinstance(result["I2"], str) else result["I2"]
    assert round(i1, 6) == round(3.0, 6)
    assert round(i2, 6) == round(2.0, 6)


def test_power_formulas():
    p1 = power_vi(5, 10)
    p2 = power_ri(5, 10)
    p3 = power_rv(5, 10)
    for p in (p1, p2, p3):
        assert isinstance(p, str)
        assert "W" in p
    assert p1.startswith("50")
    assert p2.startswith("500")
    assert p3.startswith("20")


def test_voltage_divider_equal_resistors():
    vin = 12.0
    result = voltage_divider(vin, 1000, 1000)
    assert isinstance(result, str)
    assert "V" in result
    value = float(result.split()[0])
    assert pytest.approx(value, rel=1e-9) == vin / 2


def test_current_divider_equal_resistors():
    itot = 10.0
    result = current_divider(itot, 10, 10)
    assert isinstance(result, str)
    assert "A" in result
    value = float(result.split()[0])
    assert pytest.approx(value, rel=1e-9) == itot / 2
