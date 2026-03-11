import math
import pytest

from elektropy import (
    half_wave_rectifier,
    full_wave_rectifier,
)

def test_half_wave_rectifier():
    result = half_wave_rectifier(v_peak=10.0, diode_drop=0.7, show_plot=False)
    vpk = 9.3
    assert pytest.approx(result["v_out_peak"], rel=1e-12) == vpk
    assert pytest.approx(result["v_dc"], rel=1e-12) == vpk / math.pi
    assert pytest.approx(result["v_rms"], rel=1e-12) == vpk / 2.0


def test_full_wave_rectifier_bridge():
    result = full_wave_rectifier(v_peak=10.0, diode_drop=0.7, diode_drops_in_path=2, show_plot=False)
    vpk = 8.6
    assert pytest.approx(result["v_out_peak"], rel=1e-12) == vpk
    assert pytest.approx(result["v_dc"], rel=1e-12) == 2.0 * vpk / math.pi
    assert pytest.approx(result["v_rms"], rel=1e-12) == vpk / math.sqrt(2.0)


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
