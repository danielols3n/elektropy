import math

def _rectified_metrics(v_peak: float, total_drop: float, *, full_wave: bool) -> dict[str, float]:
    """
    Compute rectifier metrics using the diode-drop-adjusted output peak.
    """
    v_out_peak = max(v_peak - total_drop, 0.0)
    if v_out_peak == 0.0:
        return {"v_out_peak": 0.0, "v_dc": 0.0, "v_rms": 0.0}

    if full_wave:
        v_dc = v_out_peak / math.pi
        v_rms = v_out_peak / math.sqrt(2.0)
    else:
        v_dc = v_out_peak / math.pi
        v_rms = v_out_peak / math.sqrt(2.0)

    return {"v_out_peak": f"{v_out_peak:.3f} V", "v_dc": f"{v_dc:.3f} V", "v_rms": f"{v_rms:.3f} V"}


def _add_metrics_box(plt, metrics: dict[str, float]) -> None:
    """
    Show the computed rectifier values directly on the plot.
    """
    lines = [
        f"Vout,peak = {metrics['v_out_peak']}",
        f"Vdc = {metrics['v_dc']}",
        f"Vrms = {metrics['v_rms']}",
    ]
    plt.gca().text(
        0.98,
        0.97,
        "\n".join(lines),
        transform=plt.gca().transAxes,
        ha="right",
        va="top",
        bbox={"boxstyle": "round", "facecolor": "white", "alpha": 0.85},
    )


def half_wave_rectifier(v_peak: float, diode_drop: float = 0.7, show_plot: bool = False) -> dict[str, float]:
    """
    Returns idealized half-wave rectifier output metrics for sinusoidal input.
    """
    if v_peak < 0:
        raise ValueError("v_peak cannot be negative.")
    if diode_drop < 0:
        raise ValueError("diode_drop cannot be negative.")

    metrics = _rectified_metrics(v_peak, diode_drop, full_wave=False)

    if show_plot:
        try:
            import matplotlib.pyplot as plt
        except ImportError as exc:
            raise ImportError(
                "matplotlib is required for show_plot=True. Install it with 'pip install matplotlib'."
            ) from exc

        periods = 3
        points = 4000
        theta = [2 * math.pi * periods * i / (points - 1) for i in range(points)]
        vin = [v_peak * math.sin(t) for t in theta]
        vout = [max(v - diode_drop, 0.0) for v in vin]

        plt.figure(figsize=(8, 4))
        plt.plot(theta, vin, label="Vin")
        plt.plot(theta, vout, label=f"Vout ({diode_drop:g} V drop)")
        plt.ylabel("Voltage (V)")
        plt.title("Half-Wave Rectifier")
        plt.grid(True, alpha=0.3)
        plt.legend(loc="lower left")
        _add_metrics_box(plt, metrics)
        plt.tight_layout()
        plt.show()

    return metrics


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

    total_drop = diode_drops_in_path * diode_drop
    metrics = _rectified_metrics(v_peak, total_drop, full_wave=True)

    if show_plot:
        try:
            import matplotlib.pyplot as plt
        except ImportError as exc:
            raise ImportError(
                "matplotlib is required for show_plot=True. Install it with 'pip install matplotlib'."
            ) from exc

        periods = 3
        points = 4000
        theta = [2 * math.pi * periods * i / (points - 1) for i in range(points)]
        vin = [v_peak * math.sin(t) for t in theta]
        vout = [max(abs(v) - diode_drops_in_path * diode_drop, 0.0) for v in vin]

        plt.figure(figsize=(8, 4))
        plt.plot(theta, vin, label="Vin")
        plt.plot(theta, vout, label=f"Vout ({total_drop:g} V total drop)")
        plt.ylabel("Voltage (V)")
        plt.title("Full-Wave Rectifier")
        plt.grid(True, alpha=0.3)
        plt.legend(loc="lower left")
        _add_metrics_box(plt, metrics)
        plt.tight_layout()
        plt.show()

    return metrics
