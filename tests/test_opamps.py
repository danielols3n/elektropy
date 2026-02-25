import pytest

from elektropy import (
    opamp_inverting_gain,
    opamp_inverting_output,
    opamp_noninverting_gain,
    opamp_noninverting_output,
    opamp_voltage_follower,
    opamp_summing_output,
    opamp_differential_output,
    opamp_integrator_output,
    opamp_differentiator_output,
    opamp_comparator,
    opamp_schmitt_thresholds,
)


def test_inverting_amplifier():
    assert opamp_inverting_gain(1000, 10000) == -10
    assert opamp_inverting_output(0.2, 1000, 10000) == -2.0


def test_noninverting_amplifier():
    assert opamp_noninverting_gain(1000, 9000) == 10
    assert opamp_noninverting_output(0.2, 1000, 9000) == 2.0


def test_voltage_follower():
    assert opamp_voltage_follower(1.234) == 1.234


def test_summing_amplifier():
    vout = opamp_summing_output([1.0, 0.5], [1000, 2000], 10000)
    assert pytest.approx(vout, rel=1e-12) == -12.5


def test_differential_amplifier():
    vout = opamp_differential_output(v_plus=1.2, v_minus=0.4, r_in=1000, r_f=10000)
    assert pytest.approx(vout, rel=1e-12) == 8.0


def test_integrator():
    vout = opamp_integrator_output(v_in=1.0, r=10000, c=1e-6, t=0.02, v_out_initial=0.0)
    assert pytest.approx(vout, rel=1e-12) == -2.0


def test_differentiator():
    vout = opamp_differentiator_output(v_in_prev=0.0, v_in_now=1.0, dt=0.001, r=10000, c=1e-6)
    assert pytest.approx(vout, rel=1e-12) == -10.0


def test_comparator():
    assert opamp_comparator(2.0, 1.0, v_high=12.0, v_low=-12.0) == 12.0
    assert opamp_comparator(0.5, 1.0, v_high=12.0, v_low=-12.0) == -12.0


def test_output_rail_limits():
    assert opamp_inverting_output(1.0, 1000, 10000, v_supply_pos=5.0, v_supply_neg=-5.0) == -5.0
    assert opamp_noninverting_output(1.0, 1000, 9000, v_supply_pos=3.3, v_supply_neg=0.0) == 3.3
    assert opamp_voltage_follower(-1.0, v_supply_pos=5.0, v_supply_neg=0.0) == 0.0
    assert opamp_summing_output([1.0, 1.0], [1000, 1000], 10000, v_supply_pos=12.0, v_supply_neg=-2.0) == -2.0
    assert opamp_differential_output(2.0, 0.0, 1000, 10000, v_supply_pos=10.0, v_supply_neg=-10.0) == 10.0
    assert opamp_integrator_output(1.0, 10000, 1e-6, 1.0, v_supply_pos=15.0, v_supply_neg=-15.0) == -15.0
    assert opamp_differentiator_output(0.0, 10.0, 0.001, 10000, 1e-6, v_supply_pos=5.0, v_supply_neg=-5.0) == -5.0


def test_schmitt_thresholds():
    thresholds = opamp_schmitt_thresholds(v_sat=15.0, r1=10000, r2=10000)
    assert pytest.approx(thresholds["upper_threshold"], rel=1e-12) == 7.5
    assert pytest.approx(thresholds["lower_threshold"], rel=1e-12) == -7.5


def test_invalid_arguments():
    with pytest.raises(ValueError):
        opamp_inverting_gain(0, 1000)
    with pytest.raises(ValueError):
        opamp_noninverting_gain(0, 1000)
    with pytest.raises(ValueError):
        opamp_summing_output([1.0], [1000, 2000], 10000)
    with pytest.raises(ValueError):
        opamp_summing_output([], [], 10000)
    with pytest.raises(ValueError):
        opamp_summing_output([1.0], [0], 10000)
    with pytest.raises(ValueError):
        opamp_integrator_output(v_in=1.0, r=1000, c=1e-6, t=-1)
    with pytest.raises(ValueError):
        opamp_differentiator_output(v_in_prev=0, v_in_now=1, dt=0, r=1000, c=1e-6)
    with pytest.raises(ValueError):
        opamp_schmitt_thresholds(v_sat=15, r1=1, r2=-1)
    with pytest.raises(ValueError):
        opamp_voltage_follower(1.0, v_supply_pos=-1.0, v_supply_neg=1.0)
