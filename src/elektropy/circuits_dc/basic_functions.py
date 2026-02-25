def power_vi(voltage, current) -> float:
    """
    Calculates power

    Arguments: voltage (float), current (float)
    Returns: power (W) -> float
    """
    return f"{float(voltage * current)} W"

def power_ri(resistance, current) -> float:
    """
    Calculates power

    Arguments: resistance (float), current (float)
    Returns: power (W) -> float
    """
    return f"{float(resistance * current**2)} W"

def power_rv(resistance, voltage) -> float:
    """
    Calculates power

    Arguments: resistance (float), voltage (float)
    Returns: power (W) -> float
    """

    if resistance == 0:
        raise ValueError("Resistance cannot be zero.")

    return f"{float((voltage**2) / resistance)} W"

def voltage_divider(V_in, R1, R2) -> float:
    """
    Calculates voltage over R1, in a voltage divider.

    Arguments: 
        * Voltage in (V_in) -> float
        * Resistor 1 (R1) -> float
        * Resistor 2 (R2) -> float

    Returns: voltage (V) -> float 
    """

    if (R1 + R2) == 0:
        raise ValueError("The sum of R1 and R2 cannot be zero.")

    return f"{float((R1 / (R1 + R2)) * V_in)} V"

def current_divider(I_in, R1, R2) -> float:
    """
    Calculates current through R1, in a current divider.

    Arguments: 
        * Current in (I_in) -> float
        * Resistor 1 (R1) -> float
        * Resistor 2 (R2) -> float

    Returns: current (I) -> float 
    """

    if (R1 + R2) == 0:
        raise ValueError("The sum of R1 and R2 cannot be zero.")

    return f"{float((R2 / (R1 + R2)) * I_in)} A"