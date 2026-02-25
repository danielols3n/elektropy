def _validate_nonzero(value: float, name: str) -> None:
    if value == 0:
        raise ValueError(f"{name} cannot be zero.")


def _apply_output_limits(v_out: float, v_supply_pos: float | None, v_supply_neg: float | None) -> float:
    if v_supply_pos is not None and v_supply_neg is not None and v_supply_pos < v_supply_neg:
        raise ValueError("v_supply_pos must be greater than or equal to v_supply_neg.")
    if v_supply_pos is not None:
        v_out = min(v_out, v_supply_pos)
    if v_supply_neg is not None:
        v_out = max(v_out, v_supply_neg)
    return v_out


def opamp_inverting_gain(r_in: float, r_f: float) -> float:
    """
    Ideal inverting amplifier gain.

    Arguments:
    r_in (float): Input resistor in ohms.
    r_f (float): Feedback resistor in ohms.

    Returns:
    float: Voltage gain (Av = -r_f / r_in).
    """
    _validate_nonzero(r_in, "r_in")
    return -r_f / r_in


def opamp_inverting_output(
    v_in: float,
    r_in: float,
    r_f: float,
    v_supply_pos: float | None = None,
    v_supply_neg: float | None = None,
) -> float:
    """
    Ideal inverting amplifier output.

    Arguments:
    v_in (float): Input voltage in volts.
    r_in (float): Input resistor in ohms.
    r_f (float): Feedback resistor in ohms.
    v_supply_pos (float | None): Positive supply rail in volts.
    v_supply_neg (float | None): Negative supply rail in volts.

    Returns:
    float: Output voltage in volts.
    """
    v_out = opamp_inverting_gain(r_in, r_f) * v_in
    return _apply_output_limits(v_out, v_supply_pos, v_supply_neg)


def opamp_noninverting_gain(r_g: float, r_f: float) -> float:
    """
    Ideal non-inverting amplifier gain.

    Arguments:
    r_g (float): Resistor from inverting input to ground in ohms.
    r_f (float): Feedback resistor in ohms.

    Returns:
    float: Voltage gain (Av = 1 + r_f / r_g).
    """
    _validate_nonzero(r_g, "r_g")
    return 1 + (r_f / r_g)


def opamp_noninverting_output(
    v_in: float,
    r_g: float,
    r_f: float,
    v_supply_pos: float | None = None,
    v_supply_neg: float | None = None,
) -> float:
    """
    Ideal non-inverting amplifier output.

    Arguments:
    v_in (float): Input voltage in volts.
    r_g (float): Resistor from inverting input to ground in ohms.
    r_f (float): Feedback resistor in ohms.
    v_supply_pos (float | None): Positive supply rail in volts.
    v_supply_neg (float | None): Negative supply rail in volts.

    Returns:
    float: Output voltage in volts.
    """
    v_out = opamp_noninverting_gain(r_g, r_f) * v_in
    return _apply_output_limits(v_out, v_supply_pos, v_supply_neg)


def opamp_voltage_follower(
    v_in: float,
    v_supply_pos: float | None = None,
    v_supply_neg: float | None = None,
) -> float:
    """
    Ideal voltage follower output.

    Arguments:
    v_in (float): Input voltage in volts.
    v_supply_pos (float | None): Positive supply rail in volts.
    v_supply_neg (float | None): Negative supply rail in volts.

    Returns:
    float: Output voltage in volts.
    """
    return _apply_output_limits(v_in, v_supply_pos, v_supply_neg)


def opamp_summing_output(
    inputs: list[float],
    input_resistors: list[float],
    r_f: float,
    v_supply_pos: float | None = None,
    v_supply_neg: float | None = None,
) -> float:
    """
    Ideal inverting summing amplifier output.

    Arguments:
    inputs (list[float]): Input voltages in volts.
    input_resistors (list[float]): Input resistors in ohms.
    r_f (float): Feedback resistor in ohms.
    v_supply_pos (float | None): Positive supply rail in volts.
    v_supply_neg (float | None): Negative supply rail in volts.

    Returns:
    float: Output voltage in volts.
    """
    if len(inputs) != len(input_resistors):
        raise ValueError("inputs and input_resistors must have the same length.")
    if len(inputs) == 0:
        raise ValueError("At least one input is required.")

    weighted_sum = 0.0
    for voltage, resistor in zip(inputs, input_resistors):
        _validate_nonzero(resistor, "input resistor")
        weighted_sum += voltage / resistor

    v_out = -r_f * weighted_sum
    return _apply_output_limits(v_out, v_supply_pos, v_supply_neg)


def opamp_differential_output(
    v_plus: float,
    v_minus: float,
    r_in: float,
    r_f: float,
    v_supply_pos: float | None = None,
    v_supply_neg: float | None = None,
) -> float:
    """
    Ideal differential amplifier output with matched resistor ratios.

    Arguments:
    v_plus (float): Non-inverting input-side signal in volts.
    v_minus (float): Inverting input-side signal in volts.
    r_in (float): Input resistor in ohms.
    r_f (float): Feedback resistor in ohms.
    v_supply_pos (float | None): Positive supply rail in volts.
    v_supply_neg (float | None): Negative supply rail in volts.

    Returns:
    float: Output voltage in volts (Vout = (r_f / r_in) * (v_plus - v_minus)).
    """
    _validate_nonzero(r_in, "r_in")
    v_out = (r_f / r_in) * (v_plus - v_minus)
    return _apply_output_limits(v_out, v_supply_pos, v_supply_neg)


def opamp_integrator_output(
    v_in: float,
    r: float,
    c: float,
    t: float,
    v_out_initial: float = 0.0,
    v_supply_pos: float | None = None,
    v_supply_neg: float | None = None,
) -> float:
    """
    Ideal inverting integrator output for constant input.

    Arguments:
    v_in (float): Constant input voltage in volts.
    r (float): Input resistor in ohms.
    c (float): Feedback capacitor in farads.
    t (float): Integration time in seconds.
    v_out_initial (float): Initial output voltage in volts.
    v_supply_pos (float | None): Positive supply rail in volts.
    v_supply_neg (float | None): Negative supply rail in volts.

    Returns:
    float: Output voltage in volts at time t.
    """
    _validate_nonzero(r, "r")
    _validate_nonzero(c, "c")
    if t < 0:
        raise ValueError("t cannot be negative.")

    v_out = v_out_initial - (v_in / (r * c)) * t
    return _apply_output_limits(v_out, v_supply_pos, v_supply_neg)


def opamp_differentiator_output(
    v_in_prev: float,
    v_in_now: float,
    dt: float,
    r: float,
    c: float,
    v_supply_pos: float | None = None,
    v_supply_neg: float | None = None,
) -> float:
    """
    Ideal inverting differentiator output from two sampled input points.

    Arguments:
    v_in_prev (float): Previous input voltage in volts.
    v_in_now (float): Current input voltage in volts.
    dt (float): Time step in seconds.
    r (float): Feedback resistor in ohms.
    c (float): Input capacitor in farads.
    v_supply_pos (float | None): Positive supply rail in volts.
    v_supply_neg (float | None): Negative supply rail in volts.

    Returns:
    float: Output voltage in volts.
    """
    _validate_nonzero(dt, "dt")
    _validate_nonzero(r, "r")
    _validate_nonzero(c, "c")
    dv_dt = (v_in_now - v_in_prev) / dt
    v_out = -(r * c) * dv_dt
    return _apply_output_limits(v_out, v_supply_pos, v_supply_neg)


def opamp_comparator(v_plus: float, v_minus: float, v_high: float = 5.0, v_low: float = 0.0) -> float:
    """
    Ideal comparator output.

    Arguments:
    v_plus (float): Non-inverting input voltage in volts.
    v_minus (float): Inverting input voltage in volts.
    v_high (float): High saturation/output level in volts.
    v_low (float): Low saturation/output level in volts.

    Returns:
    float: Comparator output level in volts.
    """
    return v_high if v_plus > v_minus else v_low


def opamp_schmitt_thresholds(v_sat: float, r1: float, r2: float) -> dict[str, float]:
    """
    Symmetric Schmitt trigger switching thresholds.

    Arguments:
    v_sat (float): Positive/negative saturation magnitude in volts.
    r1 (float): Resistor from output to non-inverting input in ohms.
    r2 (float): Resistor from non-inverting input to reference node in ohms.

    Returns:
    dict[str, float]: Upper and lower switching thresholds in volts.
    """
    _validate_nonzero(r1 + r2, "r1 + r2")
    beta = r2 / (r1 + r2)
    v_th = beta * v_sat
    return {"upper_threshold": v_th, "lower_threshold": -v_th}
