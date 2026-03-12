import pytest

from elektropy import (
    half_wave_rectifier,
    full_wave_rectifier,
)

def test_half_wave_rectifier_nonzero_diode_drop():
    result = half_wave_rectifier(v_peak=10.0, diode_drop=0.7, show_plot=False)
    vpk = 9.3
    assert pytest.approx(result["v_out_peak"], rel=1e-12) == vpk
    assert pytest.approx(result["v_dc"], rel=1e-12) == 0.318 * vpk
    assert pytest.approx(result["v_rms"], rel=1e-12) == vpk / 2.0


def test_half_wave_rectifier_zero_diode_drop_matches_ideal_formula():
    result = half_wave_rectifier(v_peak=10.0, diode_drop=0.0, show_plot=False)
    assert pytest.approx(result["v_out_peak"], rel=1e-12) == 10.0
    assert pytest.approx(result["v_dc"], rel=1e-12) == 0.318 * 10.0
    assert pytest.approx(result["v_rms"], rel=1e-12) == 10.0 / 2.0


def test_full_wave_rectifier_bridge_nonzero_diode_drop():
    result = full_wave_rectifier(v_peak=10.0, diode_drop=0.7, diode_drops_in_path=2, show_plot=False)
    vpk = 8.6
    assert pytest.approx(result["v_out_peak"], rel=1e-12) == vpk
    assert pytest.approx(result["v_dc"], rel=1e-12) == 0.636 * vpk
    assert pytest.approx(result["v_rms"], rel=1e-12) == vpk / (2.0 ** 0.5)


def test_full_wave_rectifier_zero_diode_drop_matches_ideal_formula():
    result = full_wave_rectifier(v_peak=10.0, diode_drop=0.0, diode_drops_in_path=2, show_plot=False)
    assert pytest.approx(result["v_out_peak"], rel=1e-12) == 10.0
    assert pytest.approx(result["v_dc"], rel=1e-12) == 0.636 * 10.0
    assert pytest.approx(result["v_rms"], rel=1e-12) == 10.0 / (2.0 ** 0.5)


def test_diode_invalid_arguments():
    with pytest.raises(ValueError):
        half_wave_rectifier(v_peak=-1.0)
    with pytest.raises(ValueError):
        half_wave_rectifier(v_peak=10.0, diode_drop=-0.1)
    with pytest.raises(ValueError):
        full_wave_rectifier(v_peak=-1.0)
    with pytest.raises(ValueError):
        full_wave_rectifier(v_peak=10.0, diode_drop=-0.1)
    with pytest.raises(ValueError):
        full_wave_rectifier(v_peak=10.0, diode_drops_in_path=-1)
