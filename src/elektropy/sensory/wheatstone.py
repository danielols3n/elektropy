def wheatstone_voltage(R, R1, R2, R3, Vin) -> float:
    """
    
    Calculate the output voltage of a Wheatstone bridge.
    R: Resistance of the sensor (ohms)
    R1, R2, R3: Known resistances (ohms)
    Vin: Input voltage (volts)
    Returns Vout (volts)

    """
    # Calculate the voltage at the midpoints of the two voltage dividers
    V_A = Vin * R2 / (R1 + R2)
    V_B = Vin * R3 / (R + R3)
    # Output voltage is the difference between these two voltages
    Vout = V_A - V_B
    return f"{Vout} V"

def wheatstone_balance_voltage(R, R1, Vin) -> float:
    """
    Calculate the output voltage of a Wheatstone bridge with R2 = R3, in other words a balanced Wheatstone bridge.
    R: Resistance of the sensor (ohms)
    R1: Known resistance (ohms)
    Vin: Input voltage (volts)
    Returns R2 = R3 (ohms) for balance (Vout = 0)

    """

    Vout = ((R - R1) / (R + R1)) * (Vin / 2)
    return f"{Vout} V"

def wheatstone_resistance(Vout, R1, R2, R3, Vin) -> float:
    """
    Calculate the resistance of the sensor in a Wheatstone bridge given the output voltage.

    Args:
        Vout: Output voltage (V)
        R1, R2, R3: Known resistances (Ω)
        Vin: Input voltage (V)
    Returns:
        R: Resistance of the sensor (Ω)
    Raises:
        ValueError: if Vin == 0 or R1 + R2 == 0
    """
    if Vin == 0:
        raise ValueError("Vin cannot be zero")
    if R1 + R2 == 0:
        raise ValueError("R1 + R2 cannot be zero")

    R = R1 * ((R2 * Vout + R3 * (Vin + Vout)) / (R2 * (Vin - Vout) - R3 * Vout))
    return f"{R} Ω"

def wheatstone_balance_resistance(R1, Vin, dV) -> float:
    """
    Calculate the resistance of the sensor in a balanced Wheatstone bridge given the output voltage.
    R1: Known resistance (ohms)
    Vin: Input voltage (volts)
    dV: Output voltage (volts)
    Returns R: Resistance of the sensor (ohms)

    """

    R = R1 * (1 + (4 * dV) / (Vin - 2 * dV))
    return f"{R} Ω"
    