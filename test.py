from elektropy import (
    opamp_inverting_gain,
    opamp_inverting_output,
    opamp_noninverting_gain,
    opamp_noninverting_output,
    opamp_summing_output,
    opamp_differential_output,
)

print(opamp_inverting_gain(1000, 10000))
print(opamp_inverting_output(0.2, 1000, 10000))
print(opamp_noninverting_gain(1000, 9000))
print(opamp_noninverting_output(0.2, 1000, 9000))
print(opamp_summing_output([1.0, 0.5], [1000, 2000], 10000))
print(opamp_differential_output(1.2, 0.4, 1000, 10000))