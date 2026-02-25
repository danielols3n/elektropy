import math


def impedance_r(resistance: float) -> complex:
    """
    Return the resistor impedance in ohms.

    Arguments:
    resistance (float): Resistance value in ohms.

    Returns:
    complex: Complex impedance for a resistor (R + j0).
    """
    return complex(resistance, 0.0)


def impedance_c(capacitance: float, frequency: float) -> complex:
    """
    Return the capacitor impedance in ohms for a given frequency.

    Arguments:
    capacitance (float): Capacitance in farads (must be > 0).
    frequency (float): Frequency in hertz (must be > 0).

    Returns:
    complex: Capacitive impedance Zc = 1/(j*w*C).
    """
    if capacitance <= 0:
        raise ValueError("Capacitance must be greater than zero.")
    if frequency <= 0:
        raise ValueError("Frequency must be greater than zero.")

    omega = 2 * math.pi * frequency
    return -1j / (omega * capacitance)


def impedance_l(inductance: float, frequency: float) -> complex:
    """
    Return the inductor impedance in ohms for a given frequency.

    Arguments:
    inductance (float): Inductance in henries (must be >= 0).
    frequency (float): Frequency in hertz (must be >= 0).

    Returns:
    complex: Inductive impedance Zl = j*w*L.
    """
    if inductance < 0:
        raise ValueError("Inductance cannot be negative.")
    if frequency < 0:
        raise ValueError("Frequency cannot be negative.")

    omega = 2 * math.pi * frequency
    return 1j * omega * inductance


def series_impedance(*impedances: complex) -> complex:
    """
    Return equivalent impedance for series-connected impedances.

    Arguments:
    *impedances (complex): One or more impedances in ohms.

    Returns:
    complex: Equivalent series impedance.
    """
    return sum(impedances, 0j)


def parallel_impedance(*impedances: complex) -> complex:
    """
    Return equivalent impedance for parallel-connected impedances.

    Arguments:
    *impedances (complex): One or more impedances in ohms.

    Returns:
    complex: Equivalent parallel impedance.
    """
    if len(impedances) == 0:
        raise ValueError("At least one impedance is required.")

    reciprocal = 0j
    for impedance in impedances:
        if impedance == 0:
            return 0j
        reciprocal += 1 / impedance

    if reciprocal == 0:
        raise ValueError("Parallel reciprocal sum cannot be zero.")
    return 1 / reciprocal


def phasor(magnitude: float, phase_deg: float) -> complex:
    """
    Convert magnitude and phase (degrees) to a complex phasor.

    Arguments:
    magnitude (float): Phasor magnitude.
    phase_deg (float): Phase angle in degrees.

    Returns:
    complex: Rectangular-form phasor.
    """
    angle_rad = math.radians(phase_deg)
    return complex(magnitude * math.cos(angle_rad), magnitude * math.sin(angle_rad))


def to_polar(value: complex) -> dict[str, float]:
    """
    Convert a complex value to polar form.

    Arguments:
    value (complex): Complex value in rectangular form.

    Returns:
    dict[str, float]: Dictionary with magnitude and phase in degrees.
    """
    magnitude = abs(value)
    phase_deg = math.degrees(math.atan2(value.imag, value.real))
    return {"magnitude": magnitude, "phase_deg": phase_deg}


def ac_power(
    voltage_rms: float | complex | None = None,
    current_rms: float | complex | None = None,
    voltage: float | complex | None = None,
    current: float | complex | None = None,
    values_are_rms: bool = True,
    phi_deg: float | None = None,
    impedance: complex | None = None,
) -> dict[str, float | complex]:
    """
    Calculate AC complex power.

    Arguments:
    voltage_rms (float | complex | None): RMS voltage phasor in volts.
    current_rms (float | complex | None): RMS current phasor in amperes.
    voltage (float | complex | None): Voltage value in volts (RMS if values_are_rms=True, otherwise peak).
    current (float | complex | None): Current value in amperes (RMS if values_are_rms=True, otherwise peak).
    values_are_rms (bool): Set False if voltage/current are provided as peak values.
    phi_deg (float | None): Phase angle between voltage and current in degrees.
    impedance (complex | None): Load impedance in ohms.

    Returns:
    dict[str, float | complex]: Active power (P), reactive power (Q),
    complex power (S), and power factor (pf).
    """
    if voltage_rms is not None and voltage is not None:
        raise ValueError("Provide only one of voltage_rms or voltage.")
    if current_rms is not None and current is not None:
        raise ValueError("Provide only one of current_rms or current.")

    voltage_input = voltage_rms if voltage_rms is not None else voltage
    current_input = current_rms if current_rms is not None else current

    scale = 1.0 if values_are_rms else math.sqrt(2)
    v_rms = complex(voltage_input) / scale if voltage_input is not None else None
    i_rms = complex(current_input) / scale if current_input is not None else None

    if phi_deg is not None:
        if v_rms is None or i_rms is None:
            raise ValueError("Voltage and current are required when phi_deg is provided.")
        apparent = abs(v_rms) * abs(i_rms)
        phi_rad = math.radians(phi_deg)
        active = apparent * math.cos(phi_rad)
        reactive = apparent * math.sin(phi_rad)
        pf = math.cos(phi_rad)
        return {"P": active, "Q": reactive, "S": apparent, "pf": pf}

    if v_rms is not None and i_rms is not None:
        s = v_rms * i_rms.conjugate()
    elif i_rms is not None and impedance is not None:
        s = (abs(i_rms) ** 2) * complex(impedance)
    elif v_rms is not None and impedance is not None:
        z = complex(impedance)
        if z == 0:
            raise ValueError("impedance cannot be zero.")
        s = (abs(v_rms) ** 2) / z.conjugate()
    else:
        raise ValueError(
            "Provide one valid set: (voltage/current), "
            "(current and impedance), or (voltage and impedance)."
        )

    p = s.real
    q = s.imag
    s_abs = abs(s)
    pf = p / s_abs if s_abs != 0 else 0.0
    return {"P": p, "Q": q, "S": s, "pf": pf}
