# ⚡ ElektroPy: Electronics and Digital Logic Toolkit

**ElektroPy** is a Python library for electrical engineering education and analysis. It covers basic circuit theory, sensor simulation (PT100, Wheatstone), and digital logic (truth tables, logic simplification, binary systems). Ideal for students, educators, and engineers alike.

---

## 📚 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Modules](#-modules)
  - [Circuits DC](#circuits_dc)
  - [Circuits AC](#circuits_ac)
  - [Digital Logic](#digital-logic)
  - [Analog Electronics](#analog)
  - [Sensors](#sensors)
- [Examples](#-examples)
- [Troubleshooting](#-troubleshooting)
- [Contributors](#-contributors)
- [License](#-license)

---

## ✨ Features

- 📐 **Circuit analysis**: Circuit analysis methods and helpers for both DC and AC circuits
- 🔋 **Power computations**: Power computations for both DC and AC.
- ⚙️ **Component modeling**: Thevenin/Norton equivalents for AC and DC.
- 📟 **Analog electronics**: Half wave rectifier and full wave rectifier, different types of OpAmps and gain calculations. 
- 🔧 **Sensor simulations**: PT100, RTD and Wheatstone bridge, dB calculations
- 💡 **Logic design**: Boolean simplification, truth tables
- 🔢 **Number system tools**: Binary, hexadecimal, 2's complement conversions

---

## 🛠 Installation

```bash
pip install elektropy
```

---

## 🚀 Usage

```python
from elektropy import (
    series_resistance, pt100_temperature,
    simplify_logic, truth_table,
    mesh_current, voltage_divider
)

print(series_resistance(10, 20, 30))              # 60 Ω
print(pt100_temperature(138.5))                   # Approx 100°C
print(simplify_logic("A*B! + A*B"))               # A
print(truth_table("A + B*C!", ["A", "B", "C"]))   # Returns truth table for the given expression
```

---

## 🧩 Modules

All available functions in ElektroPy are listed below. Example usages are found under [Examples](#-examples).

### 💡 Circuits DC

| Function/Class | Description |
|----------------|-------------|
| `series_resistance(*R: float)` | Calculates the total resistance of resistors connected in series. <br>**Parameters:** `*R` – one or more resistor values (Ω). <br>**Returns:** equivalent resistance as a formatted string in ohms. |
| `parallell_resistance(*R: float)` | Calculates the total resistance of resistors connected in parallel. <br>**Parameters:** `*R` – one or more resistor values (Ω). <br>**Returns:** equivalent resistance as a formatted string in ohms. |
| `power_vi(V: float, I: float)` | Calculates electrical power from voltage and current. <br>**Parameters:** `V` – voltage (V), `I` – current (A). <br>**Returns:** power as a formatted string in watts. |
| `power_ri(R: float, I: float)` | Calculates electrical power from resistance and current. <br>**Parameters:** `R` – resistance (Ω), `I` – current (A). <br>**Returns:** power as a formatted string in watts. |
| `power_rv(R: float, V: float)` | Calculates electrical power from resistance and voltage. <br>**Parameters:** `R` – resistance (Ω), `V` – voltage (V). <br>**Returns:** power as a formatted string in watts. |
| `voltage_divider(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`Vin: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`R1: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`R2: float`<br>`)` | Calculates the voltage across `R1` in a two-resistor voltage divider. <br>**Parameters:** `Vin` – input voltage (V), `R1` – first resistor (Ω), `R2` – second resistor (Ω). <br>**Returns:** output voltage as a formatted string in volts. |
| `current_divider(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`Iin: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`R1: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`R2: float`<br>`)` | Calculates the current through `R1` in a two-branch current divider. <br>**Parameters:** `Iin` – input current (A), `R1` – first branch resistance (Ω), `R2` – second branch resistance (Ω). <br>**Returns:** branch current as a formatted string in amperes. |
| `mesh_current_dc(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`equations: list[str],`<br>&nbsp;&nbsp;&nbsp;&nbsp;`variables: list[str],`<br>&nbsp;&nbsp;&nbsp;&nbsp;`decimals: int = 5`<br>`)` | Solves DC mesh-current equations symbolically. <br>**Parameters:** `equations` – SymPy-compatible equations, `variables` – unknown mesh-current names, `decimals` – rounding precision. <br>**Returns:** a dictionary mapping variable names to formatted current values in amperes. |
| `node_voltage_dc(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`equations: list[str],`<br>&nbsp;&nbsp;&nbsp;&nbsp;`variables: list[str],`<br>&nbsp;&nbsp;&nbsp;&nbsp;`decimals: int = 5`<br>`)` | Solves DC node-voltage equations symbolically. <br>**Parameters:** `equations` – SymPy-compatible equations, `variables` – unknown node-voltage names, `decimals` – rounding precision. <br>**Returns:** a dictionary mapping variable names to formatted voltage values in volts. |
| `thevenin_from_voc_isc_dc(Voc: float, Isc: float)` | Builds a DC Thevenin equivalent from open-circuit voltage and short-circuit current. <br>**Parameters:** `Voc` – open-circuit voltage (V), `Isc` – short-circuit current (A). <br>**Returns:** a `Thevenin` object. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.for_load(RL: float)` | Calculates load voltage, current, and power for a Thevenin source. <br>**Parameters:** `RL` – load resistance (Ω). <br>**Returns:** a dictionary with `V_L`, `I_L`, and `P_L`. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.max_power()` | Computes the maximum-power-transfer load for a Thevenin source. <br>**Parameters:** none. <br>**Returns:** a dictionary with optimal load resistance and maximum power. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.to_norton()` | Converts a Thevenin equivalent to a Norton equivalent. <br>**Parameters:** none. <br>**Returns:** a `Norton` object. |
| `norton_from_voc_isc_dc(Voc: float, Isc: float)` | Builds a DC Norton equivalent from open-circuit voltage and short-circuit current. <br>**Parameters:** `Voc` – open-circuit voltage (V), `Isc` – short-circuit current (A). <br>**Returns:** a `Norton` object. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.for_load(RL: float)` | Calculates load voltage, current, and power for a Norton source. <br>**Parameters:** `RL` – load resistance (Ω). <br>**Returns:** a dictionary with `V_L`, `I_L`, and `P_L`. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.max_power()` | Computes the maximum-power-transfer load for a Norton source. <br>**Parameters:** none. <br>**Returns:** a dictionary with optimal load resistance and maximum power. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.to_thevenin()` | Converts a Norton equivalent to a Thevenin equivalent. <br>**Parameters:** none. <br>**Returns:** a `Thevenin` object. |


---

### 🔌 Circuits AC

| Function/Class | Description |
|----------------|-------------|
| `impedance_r(R: float) -> complex`| Converts a resistance to resistor impedance. <br>**Parameters:** `R` – resistance (Ω). <br>**Returns:** complex impedance `R + 0j`. |
| `impedance_l(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`L: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`frequency: float \| None,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`omega: float \| None`<br>`) -> complex`| Calculates inductive impedance from inductance and either frequency or angular frequency. <br>**Parameters:** `L` – inductance (H), `frequency` – frequency (Hz), `omega` – angular frequency (rad/s). <br>**Returns:** complex inductive impedance. |
| `impedance_c(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`C: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`frequency: float \| None,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`omega: float \| None`<br>`) -> complex`| Calculates capacitive impedance from capacitance and either frequency or angular frequency. <br>**Parameters:** `C` – capacitance (F), `frequency` – frequency (Hz), `omega` – angular frequency (rad/s). <br>**Returns:** complex capacitive impedance. |
| `series_impedance(*Z: complex) -> complex` | Calculates total impedance for series-connected elements. <br>**Parameters:** `*Z` – one or more impedances (Ω). <br>**Returns:** equivalent complex impedance. |
| `parallel_impedance(*Z: complex) -> complex` | Calculates total impedance for parallel-connected elements. <br>**Parameters:** `*Z` – one or more impedances (Ω). <br>**Returns:** equivalent complex impedance. |
| `phasor(magnitude: float, phase_deg: float) -> complex` | Converts magnitude and phase to rectangular complex form. <br>**Parameters:** `magnitude` – phasor magnitude, `phase_deg` – phase angle (degrees). <br>**Returns:** complex phasor. |
| `to_polar(value: complex) -> dict[str, float]` | Converts a complex number to polar form. <br>**Parameters:** `value` – complex number in rectangular form. <br>**Returns:** a dictionary with magnitude and phase in degrees. |
| `ac_power(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`voltage: float \| complex \| None,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`current: float \| complex \| None,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`values_are_rms: bool = True,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`phi_deg: float \| None,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`impedance: complex \| None,`<br>`)` | Calculates AC apparent, active, and reactive power. <br>**Parameters:** `voltage` – voltage, `current` – current, `values_are_rms` – whether the given values are RMS, `phi_deg` – phase angle, `impedance` – load impedance. <br>**Returns:** a dictionary with `P`, `Q`, `S`, and `pf`. |
| `voltage_divider_ac(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`Vin: float \| complex,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`Z1: complex,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`Z2: complex`<br>`)` | Calculates the voltage across `Z1` in a two-impedance AC divider. <br>**Parameters:** `Vin` – input voltage, `Z1` – first impedance (Ω), `Z2` – second impedance (Ω). <br>**Returns:** complex output voltage. |
| `current_divider_ac(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`Iin: float \| complex,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`Z1: complex,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`Z2: complex`<br>`)` | Calculates the current through `Z1` in a two-branch AC divider. <br>**Parameters:** `Iin` – input current, `Z1` – first branch impedance (Ω), `Z2` – second branch impedance (Ω). <br>**Returns:** complex branch current. |
| `mesh_current_ac(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`equations: list[str],`<br>&nbsp;&nbsp;&nbsp;&nbsp;`variables: list[str],`<br>&nbsp;&nbsp;&nbsp;&nbsp;`decimals: int = 5`<br>`)` | Solves AC mesh-current equations symbolically. <br>**Parameters:** `equations` – SymPy-compatible equations, `variables` – unknown mesh-current names, `decimals` – rounding precision. <br>**Returns:** a dictionary mapping variable names to formatted current values in amperes. |
| `node_voltage_ac(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`equations: list[str],`<br>&nbsp;&nbsp;&nbsp;&nbsp;`variables: list[str],`<br>&nbsp;&nbsp;&nbsp;&nbsp;`decimals: int = 5`<br>`)` | Solves AC node-voltage equations symbolically. <br>**Parameters:** `equations` – SymPy-compatible equations, `variables` – unknown node-voltage names, `decimals` – rounding precision. <br>**Returns:** a dictionary mapping variable names to formatted voltage values in volts. |
| `thevenin_from_voc_isc_ac(Voc: float, Isc: float)` | Builds an AC Thevenin equivalent from open-circuit voltage and short-circuit current. <br>**Parameters:** `Voc` – open-circuit voltage, `Isc` – short-circuit current. <br>**Returns:** a `TheveninAC` object. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.for_load(ZL: complex)` | Calculates load voltage, current, and power for an AC Thevenin source. <br>**Parameters:** `ZL` – load impedance (Ω). <br>**Returns:** a dictionary with `V_L`, `I_L`, `S_L`, and `P_L`. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.max_power()` | Computes the conjugate-matched load for maximum power transfer. <br>**Parameters:** none. <br>**Returns:** a dictionary with optimal load impedance and maximum power. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.to_norton()` | Converts an AC Thevenin equivalent to a Norton equivalent. <br>**Parameters:** none. <br>**Returns:** a `NortonAC` object. |
| `norton_from_voc_isc_ac(Voc: float, Isc: float)` | Builds an AC Norton equivalent from open-circuit voltage and short-circuit current. <br>**Parameters:** `Voc` – open-circuit voltage, `Isc` – short-circuit current. <br>**Returns:** a `NortonAC` object. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.for_load(ZL: complex)` | Calculates load voltage, current, and power for an AC Norton source. <br>**Parameters:** `ZL` – load impedance (Ω). <br>**Returns:** a dictionary with `V_L`, `I_L`, `S_L`, and `P_L`. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.max_power()` | Computes the conjugate-matched load for maximum power transfer. <br>**Parameters:** none. <br>**Returns:** a dictionary with optimal load impedance and maximum power. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.to_thevenin()` | Converts an AC Norton equivalent to a Thevenin equivalent. <br>**Parameters:** none. <br>**Returns:** a `TheveninAC` object. |

---

### 🧠 Digital Logic

| Function | Description |
|----------|-------------|
| `binary_to_decimal(binary_str: str)` | Converts a binary string to a decimal integer. <br>**Parameters:** `binary_str` – binary input string. <br>**Returns:** decimal integer value. |
| `decimal_to_binary(number: int)` | Converts a decimal integer to a binary string. <br>**Parameters:** `number` – decimal integer. <br>**Returns:** binary string. |
| `binary_to_hexadecimal(binary_str: str)` | Converts a binary string to a hexadecimal string. <br>**Parameters:** `binary_str` – binary input string. <br>**Returns:** hexadecimal string. |
| `hexadecimal_to_binary(hex_str: str)` | Converts a hexadecimal string to a binary string. <br>**Parameters:** `hex_str` – hexadecimal input string. <br>**Returns:** binary string. |
| `decimal_to_hexadecimal(number: int)` | Converts a decimal integer to a hexadecimal string. <br>**Parameters:** `number` – decimal integer. <br>**Returns:** hexadecimal string. |
| `hexadecimal_to_decimal(hex_str: str)` | Converts a hexadecimal string to a decimal integer. <br>**Parameters:** `hex_str` – hexadecimal input string. <br>**Returns:** decimal integer value. |
| `decimal_to_twos_comp(number: int, bits: int)` | Converts a signed decimal integer to two’s complement form. <br>**Parameters:** `number` – signed decimal integer, `bits` – bit width. <br>**Returns:** binary string in two’s complement representation. |
| `twos_comp_to_decimal(binary_str: str)` | Converts a two’s complement binary string to a decimal integer. <br>**Parameters:** `binary_str` – binary input string. <br>**Returns:** signed decimal integer value. |
| `simplify_logic(expr: str)` | Simplifies a Boolean expression using SymPy. <br>**Parameters:** `expr` – logic expression in ElektroPy syntax. <br>**Returns:** simplified Boolean expression as a string. |
| `truth_table(expr: str, variables: list[str])` | Generates a Boolean truth table for a logic expression. <br>**Parameters:** `expr` – logic expression in ElektroPy syntax, `variables` – variable names used in the expression. <br>**Returns:** formatted truth table as a string. |


For the digital logic functions, `simplify_logic()` and `truth_table()`, use following notations for `AND`, `OR` and `NOT`:

&nbsp;

| Operator in Python | Equivalent | Usage |
|----------|-------------|-------------|
| `*` | AND | Use this as a normal AND in the logic expression
| `+` | OR | Use this as a normal OR in the logic expression
| `!` | NOT | Use this as a normal NOT in the logic expression

---

### 📟 Analog Electronics

| Function | Description |
|----------|-------------|
| `half_wave_rectifier(`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`v_peak: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`diode_drop: float = 0.7,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`show_plot: bool = False`<br>`)` | Calculates idealized half-wave rectifier output values for a sinusoidal input. <br>**Parameters:** `v_peak` – input peak voltage (V), `diode_drop` – forward drop per diode (V), `show_plot` – whether to display the waveform plot. <br>**Returns:** a dictionary with `v_out_peak`, `v_dc`, and `v_rms`. |
| `full_wave_rectifier(`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`v_peak: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`diode_drop: float = 0.7,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`diode_drops_in_path: int = 2,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`show_plot: bool = False`<br>`)` | Calculates idealized full-wave rectifier output values for a sinusoidal input. <br>**Parameters:** `v_peak` – input peak voltage (V), `diode_drop` – forward drop per diode (V), `diode_drops_in_path` – number of diode drops in the current path, `show_plot` – whether to display the waveform plot. <br>**Returns:** a dictionary with `v_out_peak`, `v_dc`, and `v_rms`. |
| `opamp_inverting_gain(`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`r_in: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`r_f: float`<br>`)` | Calculates the ideal inverting amplifier gain. <br>**Parameters:** `r_in` – input resistor (Ω), `r_f` – feedback resistor (Ω). <br>**Returns:** voltage gain as a float. |
| `opamp_inverting_output(`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`v_in: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`r_in: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`r_f: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`v_supply_pos: float \| None,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`v_supply_neg: float \| None`<br>`)` | Calculates the output voltage of an ideal inverting amplifier. <br>**Parameters:** `v_in` – input voltage (V), `r_in` – input resistor (Ω), `r_f` – feedback resistor (Ω), `v_supply_pos` – positive supply rail (V), `v_supply_neg` – negative supply rail (V). <br>**Returns:** output voltage as a float. |
| `opamp_noninverting_gain(`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`r_g: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`r_f: float`<br>`)` | Calculates the ideal non-inverting amplifier gain. <br>**Parameters:** `r_g` – resistor from inverting input to ground (Ω), `r_f` – feedback resistor (Ω). <br>**Returns:** voltage gain as a float. |
| `opamp_noninverting_output(`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`v_in: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`r_g: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`r_f: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`v_supply_pos: float \| None,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`v_supply_neg: float \| None`<br>`)` | Calculates the output voltage of an ideal non-inverting amplifier. <br>**Parameters:** `v_in` – input voltage (V), `r_g` – resistor from inverting input to ground (Ω), `r_f` – feedback resistor (Ω), `v_supply_pos` – positive supply rail (V), `v_supply_neg` – negative supply rail (V). <br>**Returns:** output voltage as a float. |
| `opamp_summing_output(`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`inputs: list[float],`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`input_resistors: list[float],`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`r_f: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`v_supply_pos: float \| None,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`v_supply_neg: float \| None`<br>`)` | Calculates the output voltage of an ideal inverting summing amplifier. <br>**Parameters:** `inputs` – input voltages (V), `input_resistors` – resistor for each input (Ω), `r_f` – feedback resistor (Ω), `v_supply_pos` – positive supply rail (V), `v_supply_neg` – negative supply rail (V). <br>**Returns:** output voltage as a float. |
| `opamp_differential_output(`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`v_plus: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`v_minus: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`r_in: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`r_f: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`v_supply_pos: float \| None,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`v_supply_neg: float \| None`<br>`)` | Calculates the output voltage of an ideal differential amplifier. <br>**Parameters:** `v_plus` – non-inverting input voltage (V), `v_minus` – inverting input voltage (V), `r_in` – input resistor (Ω), `r_f` – feedback resistor (Ω), `v_supply_pos` – positive supply rail (V), `v_supply_neg` – negative supply rail (V). <br>**Returns:** output voltage as a float. |

---

### 🌡️ Sensors

#### PT100 (RTD)

| Function | Description |
|----------|-------------|
| `pt100_resistance(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`temperature_celsius: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`R0: float = 100.0,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`A: float = 3.9083e-3,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`B: float = -5.775e-7`<br>`) -> str` | Calculates PT100 sensor resistance from temperature using the Callendar-Van Dusen model. <br>**Parameters:** `temperature_celsius` – temperature (°C), `R0` – nominal resistance at 0 °C (Ω), `A` and `B` – PT100 coefficients. <br>**Returns:** resistance as a formatted string in ohms. |
| `pt100_temperature(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`resistance_ohms: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`R0: float = 100.0,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`A: float = 3.9083e-3,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`B: float = -5.775e-7`<br>`) -> str` | Calculates PT100 temperature from measured resistance using the inverse Callendar-Van Dusen relation. <br>**Parameters:** `resistance_ohms` – measured resistance (Ω), `R0` – nominal resistance at 0 °C (Ω), `A` and `B` – PT100 coefficients. <br>**Returns:** both quadratic temperature solutions as formatted strings. |


#### Wheatstone Bridge

| Function | Description |
|----------|-------------|
| `wheatstone_voltage(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`R: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`R1: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`R2: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`R3: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`Vin: float`<br>`) -> float` | Calculates the output voltage of a general Wheatstone bridge. <br>**Parameters:** `R` – sensor resistance (Ω), `R1`, `R2`, `R3` – known resistors (Ω), `Vin` – input voltage (V). <br>**Returns:** output voltage as a formatted string in volts. |
| `wheatstone_balance_voltage(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`R: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`R1: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`Vin: float`<br>`) -> float` | Calculates the output voltage of a balanced Wheatstone bridge where `R2 = R3`. <br>**Parameters:** `R` – sensor resistance (Ω), `R1` – known resistance (Ω), `Vin` – input voltage (V). <br>**Returns:** output voltage as a formatted string in volts. |
| `wheatstone_resistance(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`Vout: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`R1: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`R2: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`R3: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`Vin: float`<br>`) -> float` | Calculates sensor resistance from the measured Wheatstone bridge output voltage. <br>**Parameters:** `Vout` – output voltage (V), `R1`, `R2`, `R3` – known resistors (Ω), `Vin` – input voltage (V). <br>**Returns:** resistance as a formatted string in ohms. |
| `wheatstone_balance_resistance(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`R1: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`Vin: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`dV: float`<br>`) -> float` | Calculates sensor resistance in a balanced Wheatstone bridge from the differential bridge voltage. <br>**Parameters:** `R1` – known resistor (Ω), `Vin` – input voltage (V), `dV` – measured bridge voltage (V). <br>**Returns:** resistance as a formatted string in ohms. |

#### dB Helpers

| Function | Description |
|----------|-------------|
| `db_power(power_in: float, power_out: float)` | Calculates power gain in decibels. <br>**Parameters:** `power_in` – input power, `power_out` – output power. <br>**Returns:** gain in dB as a float. |
| `db_voltage(voltage_in: float, voltage_out: float)` | Calculates voltage gain in decibels. <br>**Parameters:** `voltage_in` – input voltage, `voltage_out` – output voltage. <br>**Returns:** gain in dB as a float. |

---

## 🧪 Examples

### 💡 Circuits DC: Resistance, Dividers, and Power

```python
from elektropy import (
    series_resistance,
    parallell_resistance,
    voltage_divider,
    current_divider,
    power_vi,
    power_ri,
    power_rv,
)

print(series_resistance(10, 20, 30))
print(parallell_resistance(10, 20))
print(voltage_divider(12, 1000, 1000))
print(current_divider(10, 10, 10))
print(power_vi(12, 0.5))
print(power_ri(10, 2))
print(power_rv(10, 12))
```

### 🧮 Circuits DC: Node Voltage and Mesh Current

```python
from elektropy import node_voltage_dc, mesh_current_dc

print(node_voltage_dc(["u1/6 + u2/8 -5", "u2/8 + 2"], ["u1", "u2"]))

print(mesh_current_dc(["i1/4 + i2/6 - 5", "i1/4 - 22"], ["i1", "i2"]))
```

### 🔁 Circuits DC: Thevenin and Norton

```python
from elektropy import thevenin_from_voc_isc_dc, norton_from_voc_isc_dc

th = thevenin_from_voc_isc_dc(10, 2)
print(th.for_load(10))
print(th.max_power())
print(th.to_norton())

no = norton_from_voc_isc_dc(10, 2)
print(no.for_load(10))
print(no.max_power())
print(no.to_thevenin())
```

### 🔌 Circuits AC: Impedance, Dividers, Phasors, and Power

```python
import math
from elektropy import (
    impedance_r,
    impedance_c,
    impedance_l,
    series_impedance,
    parallel_impedance,
    voltage_divider_ac,
    current_divider_ac,
    phasor,
    to_polar,
    ac_power,
)

omega = 2 * math.pi * 50
z_r = impedance_r(10)
z_c = impedance_c(10e-6, omega=omega)
z_l = impedance_l(0.1, frequency=50)
print(z_r, z_c, z_l)
print(series_impedance(z_r, z_l))
print(parallel_impedance(z_r, z_l))
print(to_polar(voltage_divider_ac(100 + 0j, 10 + 5j, 20 - 5j)))
print(current_divider_ac(10 + 0j, 10 + 5j, 20 - 5j))



p = phasor(10, 30)
print(p, to_polar(p))
print(ac_power(voltage=230, current=5, phi_deg=36.87))
print(ac_power(current=4 - 3j, impedance=36.8 + 27.6j, values_are_rms=False))
```

### 🔄 Circuits AC: Node Voltage and Mesh Current

```python
from elektropy import node_voltage_ac, mesh_current_ac

print(node_voltage_ac(["-5 + u1/(4-3j)", "10 - u2/(4+8j)"], ["u1", "u2"]))
print(mesh_current_ac(["-5 + i1/(4+3j)", "10 - i2/(4-8j)"], ["i1", "i2"]))

```

### 🔁 Circuits AC: Thevenin and Norton

```python
from elektropy import thevenin_from_voc_isc_ac, norton_from_voc_isc_ac

th = thevenin_from_voc_isc_ac(12 + 6j, 3 - 1j)
print(th.Zth)
print(th.for_load(10 + 2j))
print(th.max_power())
print(th.to_norton())

no = norton_from_voc_isc_ac(12 + 6j, 3 - 1j)
print(no.for_load(10 + 2j))
print(no.max_power())
print(no.to_thevenin())
```

### 📟 Analog Electronics: Op-Amps

```python
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
```

### 🔋 Analog Electronics: Rectifiers

```python
from elektropy import half_wave_rectifier, full_wave_rectifier

print(half_wave_rectifier(10.0, diode_drop=0.7))
print(full_wave_rectifier(10.0, diode_drop=0.7, diode_drops_in_path=2))

# Optional plots:
print(half_wave_rectifier(10.0, diode_drop=0.7, show_plot=True))
print(full_wave_rectifier(10.0, diode_drop=0.7, diode_drops_in_path=2, show_plot=True))
```

### 🌡️ Sensors: PT100

```python
from elektropy import pt100_resistance, pt100_temperature

print(pt100_resistance(100))
print(pt100_temperature(138.5))
```

### 🌡️ Sensors: Wheatstone Bridge

```python
from elektropy import (
    wheatstone_voltage,
    wheatstone_balance_voltage,
    wheatstone_resistance,
    wheatstone_balance_resistance,
)

print(wheatstone_voltage(120, 100, 100, 100, 5))
print(wheatstone_balance_voltage(102, 100, 5))
print(wheatstone_resistance(0.1, 100, 100, 100, 5))
print(wheatstone_balance_resistance(100, 5, 0.02))
```

### 🔊 Sensors: dB Helpers

```python
from elektropy import db_power, db_voltage

print(db_power(1.0, 10.0))   # 10 dB
print(db_voltage(1.0, 10.0)) # 20 dB
```

### 🧠 Digital Logic: Simplification and Truth Table

```python
from elektropy import simplify_logic, truth_table

print(simplify_logic("A*B + A*B!"))  # A
print(truth_table("A + B*C!", ["A", "B", "C"]))
```

### 🔢 Digital Logic: Number System Conversions

```python
from elektropy import (
    binary_to_decimal,
    decimal_to_binary,
    binary_to_hexadecimal,
    hexadecimal_to_binary,
    decimal_to_hexadecimal,
    hexadecimal_to_decimal,
    decimal_to_twos_comp,
    twos_comp_to_decimal,
)

print(binary_to_decimal("1101"))
print(decimal_to_binary(13))
print(binary_to_hexadecimal("11111111"))
print(hexadecimal_to_binary("FF"))
print(decimal_to_hexadecimal(255))
print(hexadecimal_to_decimal("FF"))
print(decimal_to_twos_comp(-5, 8))
print(twos_comp_to_decimal("11111011"))
```

---

## 🧯 Troubleshooting

| Problem | Solution |
|---------|----------|
| `No solution found` | Check linear independence of equations |
| Logic errors | Ensure Boolean expressions use correct digital syntax: `!` = NOT, `*` = AND, `+` = OR, `~` = XOR |
| PT100 out-of-range | `pt100_temperature()` raises a `ValueError` for resistance values outside the supported PT100 model range |
| `show_plot=True` fails in diode functions | Install `matplotlib`, or call `half_wave_rectifier()` / `full_wave_rectifier()` with `show_plot=False` |
| Divider, power, dB, or op-amp functions raise `ValueError` | Check for zero or invalid inputs such as `R=0`, `R1 + R2 = 0`, non-positive dB inputs, or invalid supply limits |
| AC impedance helpers raise `ValueError` | Pass exactly one of `frequency` or `omega`, and keep capacitance positive and frequency/omega in valid range |
| A function returns a string instead of a number | Several DC and sensor helpers return formatted strings with units like `\"10.0 W\"` or `\"60 Ω\"`; parse the numeric part before reusing the result in calculations |
| `truth_table()` shows `Error: ...` inside the table | The expression could not be evaluated; check syntax and variable names because errors are embedded in the output instead of being raised |
| `parallel_resistance` import fails | The public API currently exports `parallell_resistance` with a double `l`, so use that exact name |
| Unexpected unit characters like `Î©` or `â„ƒ` | This is a text encoding issue in parts of the library output; treat it as cosmetic or normalize the string before display |

---


## 🗺️ Roadmap

This library is under continuous development. Some of the planned features are listed below. These will be made public once they have been developed and thoroughly tested. 

- Add transformer calculations
- Add transistor calculations and helpers
- Improve plotting options
- low-pass and high-pass filters
- Laplace transform helpers
- Sampling helpers

---

## 👥 Contributors

- **Daniel Olsen** – Project author  
- **184446@stud.hvl.no** - Support

If you find any bugs, errors, or spelling mistakes, please contact me at the email address above. Any feedback or contributions are appreciated!

---

## 📄 License

MIT License – see the [LICENSE](LICENSE) file for full text.
