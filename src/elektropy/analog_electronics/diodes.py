import math

def half_wave_rectifier(v_peak: float, diode_drop: float = 0.7, show_plot: bool = False) -> dict[str, float]:
    """
    Returns idealized half-wave rectifier output metrics for sinusoidal input.
    """
    if v_peak < 0:
        raise ValueError("v_peak cannot be negative.")
    if diode_drop < 0:
        raise ValueError("diode_drop cannot be negative.")

    v_out_peak = max(v_peak - diode_drop, 0.0)
    v_dc = v_out_peak / math.pi
    v_rms = v_out_peak / 2.0

    if show_plot:
        try:
            import matplotlib.pyplot as plt
        except ImportError as exc:
            raise ImportError(
                "matplotlib is required for show_plot=True. Install it with 'pip install matplotlib'."
            ) from exc

        points = 1000
        theta = [2 * math.pi * i / (points - 1) for i in range(points)]
        vin = [v_peak * math.sin(t) for t in theta]
        vout = [max(v - diode_drop, 0.0) for v in vin]

        plt.figure(figsize=(8, 4))
        plt.plot(theta, vin, label="Vin")
        plt.plot(theta, vout, label="Vout (half-wave)")
        plt.xlabel("Electrical angle (rad)")
        plt.ylabel("Voltage (V)")
        plt.title("Half-Wave Rectifier")
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.tight_layout()
        plt.show()

    return {"v_out_peak": v_out_peak, "v_dc": v_dc, "v_rms": v_rms}


def full_wave_rectifier(
    v_peak: float,
    diode_drop: float = 0.7,
    diode_drops_in_path: int = 2,
    show_plot: bool = False,
) -> dict[str, float]:
    """
    Return idealized full-wave rectifier output metrics for sinusoidal input.
    """
    if v_peak < 0:
        raise ValueError("v_peak cannot be negative.")
    if diode_drop < 0:
        raise ValueError("diode_drop cannot be negative.")
    if diode_drops_in_path < 0:
        raise ValueError("diode_drops_in_path cannot be negative.")

    v_out_peak = max(v_peak - diode_drops_in_path * diode_drop, 0.0)
    v_dc = (2.0 * v_out_peak) / math.pi
    v_rms = v_out_peak / math.sqrt(2.0)

    if show_plot:
        try:
            import matplotlib.pyplot as plt
        except ImportError as exc:
            raise ImportError(
                "matplotlib is required for show_plot=True. Install it with 'pip install matplotlib'."
            ) from exc

        points = 1000
        theta = [2 * math.pi * i / (points - 1) for i in range(points)]
        vin = [v_peak * math.sin(t) for t in theta]
        vout = [max(abs(v) - diode_drops_in_path * diode_drop, 0.0) for v in vin]

        plt.figure(figsize=(8, 4))
        plt.plot(theta, vin, label="Vin")
        plt.plot(theta, vout, label="Vout (full-wave)")
        plt.xlabel("Electrical angle (rad)")
        plt.ylabel("Voltage (V)")
        plt.title("Full-Wave Rectifier")
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.tight_layout()
        plt.show()

    return {"v_out_peak": v_out_peak, "v_dc": v_dc, "v_rms": v_rms}
