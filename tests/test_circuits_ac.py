import sympy as sp
import pytest

from elektropy import (
    mesh_current_ac,
    node_voltage_ac,
    impedance_r,
    impedance_c,
    impedance_l,
    series_impedance,
    parallel_impedance,
    phasor,
    to_polar,
    ac_power,
)


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


def test_impedance_helpers():
    zr = impedance_r(10)
    zc = impedance_c(10e-6, 50)
    zl = impedance_l(0.1, 50)

    assert zr == 10 + 0j
    assert abs(zc - (-318.3098861837907j)) < 1e-9
    assert abs(zl - (31.415926535897935j)) < 1e-9


def test_series_parallel_impedance():
    z1 = 10 + 5j
    z2 = 20 - 5j

    zs = series_impedance(z1, z2)
    zp = parallel_impedance(z1, z2)

    assert zs == 30 + 0j
    assert abs(zp - (7.5 + 1.6666666666666667j)) < 1e-12


def test_phasor_and_polar():
    z = phasor(10, 30)
    polar = to_polar(z)

    assert abs(z - (8.660254037844387 + 5j)) < 1e-12
    assert abs(polar["magnitude"] - 10) < 1e-12
    assert abs(polar["phase_deg"] - 30) < 1e-12


def test_ac_power():
    result = ac_power(230, 5, 36.86989764584402)
    assert pytest.approx(result["S"], rel=1e-9) == 1150
    assert pytest.approx(result["P"], rel=1e-9) == 920
    assert pytest.approx(result["Q"], rel=1e-9) == 690
    assert pytest.approx(result["pf"], rel=1e-9) == 0.8


def test_ac_power_with_peak_values():
    v_peak = 230 * (2 ** 0.5)
    i_peak = 5 * (2 ** 0.5)
    result = ac_power(voltage=v_peak, current=i_peak, phi_deg=36.86989764584402, values_are_rms=False)
    assert pytest.approx(result["S"], rel=1e-9) == 1150
    assert pytest.approx(result["P"], rel=1e-9) == 920
    assert pytest.approx(result["Q"], rel=1e-9) == 690


def test_ac_power_complex_from_v_and_i():
    result = ac_power(voltage_rms=230 + 0j, current_rms=4 - 3j)
    assert pytest.approx(result["P"], rel=1e-9) == 920
    assert pytest.approx(result["Q"], rel=1e-9) == 690
    assert abs(result["S"] - (920 + 690j)) < 1e-9


def test_ac_power_complex_from_i_and_z():
    result = ac_power(current_rms=4 - 3j, impedance=36.8 + 27.6j)
    assert pytest.approx(result["P"], rel=1e-9) == 920
    assert pytest.approx(result["Q"], rel=1e-9) == 690
    assert abs(result["S"] - (920 + 690j)) < 1e-9


def test_ac_power_complex_from_v_and_z():
    result = ac_power(voltage_rms=230 + 0j, impedance=36.8 + 27.6j)
    assert pytest.approx(result["P"], rel=1e-9) == 920
    assert pytest.approx(result["Q"], rel=1e-9) == 690
    assert abs(result["S"] - (920 + 690j)) < 1e-9


def test_invalid_impedance_inputs():
    with pytest.raises(ValueError):
        impedance_c(0, 50)
    with pytest.raises(ValueError):
        impedance_c(10e-6, 0)
    with pytest.raises(ValueError):
        impedance_l(-1, 50)
    with pytest.raises(ValueError):
        impedance_l(1, -50)
    with pytest.raises(ValueError):
        parallel_impedance()
    with pytest.raises(ValueError):
        ac_power(voltage_rms=230)
    with pytest.raises(ValueError):
        ac_power(voltage_rms=230, impedance=0)
    with pytest.raises(ValueError):
        ac_power(voltage_rms=230, voltage=230)
    with pytest.raises(ValueError):
        ac_power(current_rms=5, current=5)
