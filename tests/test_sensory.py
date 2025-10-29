import pytest
from elektropy import (
    wheatstone_voltage,
    wheatstone_balance_voltage,
    wheatstone_resistance,
    wheatstone_balance_resistance,
    pt100_temperature,
    pt100_resistance,
)


def test_wheatstone_voltage_balanced():
    R = 100.0
    R1 = R2 = R3 = 100.0
    Vin = 5.0
    vout = wheatstone_voltage(R, R1, R2, R3, Vin)
    assert pytest.approx(vout, rel=1e-9) == 0.0


def test_wheatstone_voltage_unbalanced():
    R = 150.0
    R1 = 100.0
    R2 = 100.0
    R3 = 100.0
    Vin = 5.0
    # expected: V_A = Vin * R2/(R1+R2) = 2.5
    #           V_B = Vin * R3/(R + R3) = 5 * 100 / 250 = 2.0
    # Vout = V_A - V_B = 0.5
    vout = wheatstone_voltage(R, R1, R2, R3, Vin)
    assert pytest.approx(vout, rel=1e-9) == 0.5


def test_wheatstone_balance_voltage():
    R = 120.0
    R1 = 100.0
    Vin = 5.0
    expected = ((R - R1) / (R + R1)) * (Vin / 2)
    vout = wheatstone_balance_voltage(R, R1, Vin)
    assert pytest.approx(vout, rel=1e-9) == expected


def test_wheatstone_resistance_roundtrip():
    R = 150.0
    R1 = 100.0
    R2 = 100.0
    R3 = 100.0
    Vin = 5.0
    vout = wheatstone_voltage(R, R1, R2, R3, Vin)
    R_calc = wheatstone_resistance(vout, R1, R2, R3, Vin)
    assert pytest.approx(R_calc, rel=1e-9) == R

def test_wheatstone_resistance_invalid_inputs():
    # Vin == 0 should raise
    with pytest.raises(ValueError, match="Vin cannot be zero"):
        wheatstone_resistance(0.1, 100.0, 100.0, 100.0, 0.0)

    # R1 + R2 == 0 should raise
    with pytest.raises(ValueError, match="R1 \+ R2 cannot be zero"):
        wheatstone_resistance(0.1, -50.0, 50.0, 100.0, 5.0)


def test_wheatstone_balance_resistance_roundtrip():
    R1 = 100.0
    Vin = 5.0
    dV = 0.1
    R_calc = wheatstone_balance_resistance(R1, Vin, dV)
    # feeding back into balance voltage should reproduce dV
    vout = wheatstone_balance_voltage(R_calc, R1, Vin)
    assert pytest.approx(vout, rel=1e-9) == dV


# pt100 (RTD) tests
def test_pt100_resistance_known_points():
    # Expected values as strings with Ω symbol
    r0 = pt100_resistance(0.0)
    r100 = pt100_resistance(100.0)

    # The function returns a string like "138.505 Ω"
    assert isinstance(r0, str)
    assert "Ω" in r0
    assert "100" in r0  # should include "100"
    assert isinstance(r100, str)
    assert "Ω" in r100
    # it should contain something close to 138.5
    assert "138" in r100 or "139" in r100


def test_pt100_temperature_roundtrip():
    temps = [-50.0, 0.0, 25.0, 100.0]
    for t in temps:
        r = pt100_resistance(t)
        t_calc_set = pt100_temperature(float(r.split()[0]))  # extract numeric part from "xxx Ω"
        
        # ensure it's a set with two readable strings
        assert isinstance(t_calc_set, set)
        assert any("Solution 1" in s for s in t_calc_set)
        assert any("Solution 2" in s for s in t_calc_set)
        assert all("℃" in s for s in t_calc_set)