from elektropy import (
    mesh_current,
    power_vi,
    power_ri,
    power_rv,
    voltage_divider,
    current_divider,
    series_resistance,
    parallell_resistance,
    thevenin_from_voc_isc,
    norton_from_voc_isc,
    truth_table,
    simplify_logic,
    binary_to_decimal, 
    decimal_to_binary,
    binary_to_hexadecimal,
    hexadecimal_to_binary, 
    decimal_to_twos_comp,
    twos_comp_to_decimal,
    decimal_to_hexadecimal,
    hexadecimal_to_decimal,
    pt100_resistance,
    pt100_temperature, 
    wheatstone_balance_resistance,
    wheatstone_balance_voltage, 
    wheatstone_resistance, 
    wheatstone_voltage
)


print(mesh_current(["-12 + 22e3*I1 + 8.2e3*(I1 - I2)", "8.2e3*(I2 - I1) + 15e3*I3 + 10e3*I2", "I2 - I3 - 10e-3"], ["I1", "I2", "I3"]))

print(power_vi(10, 2))
print(power_ri(5, 3))
print(power_rv(10, 20))
print(voltage_divider(12, 1000, 2000))
print(current_divider(0.03, 1000, 2000))

""" print(current_divider(0.03, 0, 0))  # This will raise a ValueError """
""" print(voltage_divider(12, 0, 0))  # This will raise a ValueError """
""" print(power_rv(0, 20))  # This will raise a ValueError """

print(series_resistance(100, 200, 300))
print(parallell_resistance(100, 200, 300))
""" print(parallell_resistance(0, 0, 0)) """

print(norton_from_voc_isc(52, 8.66666667))
print(truth_table('A*B + A!*C', ["A", "B", "C"]))
print(simplify_logic('A!*B + A*C'))

print("binary_to_decimal('1011') ->", binary_to_decimal('1011'))
print("decimal_to_binary(13) ->", decimal_to_binary(13))
print("binary_to_hexadecimal('11110000') ->", binary_to_hexadecimal('11110000'))
print("hexadecimal_to_binary('AF') ->", hexadecimal_to_binary('AF'))
print("decimal_to_twos_comp(-5, 8) ->", decimal_to_twos_comp(-5, 8))
print("twos_comp_to_decimal('11111011') ->", twos_comp_to_decimal('11111011'))
print("decimal_to_hexadecimal(255) ->", decimal_to_hexadecimal(255))
print("hexadecimal_to_decimal('FF') ->", hexadecimal_to_decimal('FF'))

print(pt100_temperature(150))
print(pt100_resistance(99.985))

print("wheatstone_balance_resistance(1000, 1000, 1000) ->", wheatstone_balance_resistance(150, 10, -0.199))
print("wheatstone_balance_voltage(1000, 1000, 1000) ->", wheatstone_balance_voltage(150, 150, 10))
print("wheatstone_resistance(1000, 1000, 1000, 5.0, 0.0) ->", wheatstone_resistance(-0.199, 150, 150, 150, 10.0))
print("wheatstone_voltage(1000, 1000, 1000, 1000, 5.0) ->", wheatstone_voltage(138.5, 150, 150, 150, 10.0))