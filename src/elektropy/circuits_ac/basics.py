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


def _resolve_omega(
    frequency: float | None,
    omega: float | None,
    *,
    allow_zero: bool,
) -> float:
    """
    Resolve angular frequency from either frequency (Hz) or omega (rad/s).
    """
    if (frequency is None) == (omega is None):
        raise ValueError("Provide exactly one of frequency or omega.")

    if frequency is not None:
        if allow_zero:
            if frequency < 0:
                raise ValueError("Frequency cannot be negative.")
        else:
            if frequency <= 0:
                raise ValueError("Frequency must be greater than zero.")
        return 2 * math.pi * frequency

    assert omega is not None
    if allow_zero:
        if omega < 0:
            raise ValueError("Omega cannot be negative.")
    else:
        if omega <= 0:
            raise ValueError("Omega must be greater than zero.")
    return omega


def impedance_c(capacitance: float, frequency: float | None = None, omega: float | None = None) -> complex:
    """
    Return the capacitor impedance in ohms.

    Arguments:
    capacitance (float): Capacitance in farads (must be > 0).
    frequency (float | None): Frequency in hertz (must be > 0).
    omega (float | None): Angular frequency in rad/s (must be > 0).

    Returns:
    complex: Capacitive impedance Zc = 1/(j*w*C).
    """
    if capacitance <= 0:
        raise ValueError("Capacitance must be greater than zero.")

    omega_value = _resolve_omega(frequency=frequency, omega=omega, allow_zero=False)
    return -1j / (omega_value * capacitance)


def impedance_l(inductance: float, frequency: float | None = None, omega: float | None = None) -> complex:
    """
    Return the inductor impedance in ohms.

    Arguments:
    inductance (float): Inductance in henries (must be >= 0).
    frequency (float | None): Frequency in hertz (must be >= 0).
    omega (float | None): Angular frequency in rad/s (must be >= 0).

    Returns:
    complex: Inductive impedance Zl = j*w*L.
    """
    if inductance < 0:
        raise ValueError("Inductance cannot be negative.")

    omega_value = _resolve_omega(frequency=frequency, omega=omega, allow_zero=True)
    return 1j * omega_value * inductance


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
    return {"Magnitude": magnitude, "Phase_deg": phase_deg}


def ac_power(
    voltage: float | complex | None = None,
    current: float | complex | None = None,
    values_are_rms: bool = True,
    phi_deg: float | None = None,
    impedance: complex | None = None,
) -> dict[str, float | complex]:
    """
    Calculate AC complex power.

    Arguments:
    voltage (float | complex | None): Voltage value in volts (RMS if values_are_rms=True, otherwise peak).
    current (float | complex | None): Current value in amperes (RMS if values_are_rms=True, otherwise peak).
    values_are_rms (bool): Set False if voltage/current are provided as peak values.
    phi_deg (float | None): Phase angle between voltage and current in degrees.
    impedance (complex | None): Load impedance in ohms.

    Returns:
    dict[str, float | complex]: Active power (P), reactive power (Q),
    complex power (S), and power factor (pf).
    """
    scale = 1.0 if values_are_rms else math.sqrt(2)
    v_rms = complex(voltage) / scale if voltage is not None else None
    i_rms = complex(current) / scale if current is not None else None

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

def voltage_divider_ac(Vin: float | complex, Z1: complex, Z2: complex) -> complex:
    """
    Calculate the output voltage of an AC voltage divider.

    Arguments:
    Vin (float | complex): Input voltage in volts.
    Z1 (complex): Impedance of the first element in ohms.
    Z2 (complex): Impedance of the second element in ohms.

    Returns:
    complex: Output voltage across Z1 in volts.
    """
    if Z1 + Z2 == 0:
        raise ValueError("Total impedance cannot be zero.")
    return Vin * (Z1 / (Z1 + Z2))

def current_divider_ac(Iin: float | complex, Z1: complex, Z2: complex) -> complex:
    """
    Calculate the output current of an AC current divider.

    Arguments:
    Iin (float | complex): Input current in amperes.
    Z1 (complex): Impedance of the first branch in ohms.
    Z2 (complex): Impedance of the second branch in ohms.

    Returns:
    complex: Output current through Z1 in amperes.
    """
    if Z1 + Z2 == 0:
        raise ValueError("Total impedance cannot be zero.")
    return Iin * (Z2 / (Z1 + Z2))