import math

def db_power(power_in: float, power_out: float) -> float:
    """
    Calculate the power gain in decibels.

    Arguments:
    power_in (float): Input power.
    power_out (float): Output power.

    Returns:
    float: Power gain in decibels.
    """
    if power_in <= 0:
        raise ValueError("power_in must be greater than zero.")
    if power_out <= 0:
        raise ValueError("power_out must be greater than zero.")

    return 10 * math.log10(power_out / power_in)

def db_voltage(voltage_in: float, voltage_out: float) -> float:
    """
    Calculate the voltage gain in decibels.

    Arguments:
    voltage_in (float): Input voltage.
    voltage_out (float): Output voltage.

    Returns:
    float: Voltage gain in decibels.
    """
    if voltage_in <= 0:
        raise ValueError("voltage_in must be greater than zero.")
    if voltage_out <= 0:
        raise ValueError("voltage_out must be greater than zero.")

    return 20 * math.log10(voltage_out / voltage_in)

