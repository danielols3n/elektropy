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
| `series_resistance(*R: float)` | Calculates the **total resistance** of resistors connected in **series**. |
| `parallel_resistance(*R: float)` | Calculates the **total resistance** of resistors connected in **parallel**. |
| `power_vi(V: float, I: float)` | Computes **power (W)** using voltage and current: *P = V × I*. |
| `power_ri(R: float, I: float)` | Computes **power (W)** using resistance and current: *P = I² × R*. |
| `power_rv(R: float, V: float)` | Computes **power (W)** using resistance and voltage: *P = V² / R*. |
| `voltage_divider(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`Vin: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;` R1: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;` R2: float`<br>`)` | Calculates the **voltage across R1** in a two-resistor voltage divider. |
| `current_divider_dc(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`Iin: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;` R1: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;` R2: float`<br>`)` | Calculates the **current through R1** in a two-branch current divider. |
| `mesh_current_dc(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`equations: list[str],`<br>&nbsp;&nbsp;&nbsp;&nbsp;` variables: list[str],`<br>&nbsp;&nbsp;&nbsp;&nbsp;` decimals: int (default: 5)`<br>`)` | Solves for **mesh currents** symbolically using a system of equations. |
| `node_voltage(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`equations: list[str],`<br>&nbsp;&nbsp;&nbsp;&nbsp;` variables: list[str],`<br>&nbsp;&nbsp;&nbsp;&nbsp;` decimals: int (default: 5)`<br>`)` | Solves for **node voltages** symbolically using a system of equations. |
| `thevenin_from_voc_isc_dc(Voc: float, Isc: float)` | Builds a **Thevenin equivalent circuit** from open-circuit voltage (`Voc`) and short-circuit current (`Isc`). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.for_load(RL: float)` | Calculates **load voltage**, **current**, and **power** for a given load resistance `RL`. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.max_power()` | Computes the **load resistance (RL)** and **power** for **maximum power transfer**. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.to_norton()` | Converts a Thevenin equivalent to its **Norton equivalent**. |
| `norton_from_voc_isc_dc(Voc: float, Isc: float)` | Builds a **Norton equivalent circuit** from open-circuit voltage (`Voc`) and short-circuit current (`Isc`). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.for_load(RL: float)` | Calculates **load voltage**, **current**, and **power** for a given load resistance `RL`. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.max_power()` | Computes the **load resistance (RL)** and **power** for **maximum power transfer**. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.to_thevenin()` | Converts a Norton equivalent to its **Thevenin equivalent**. |


---

### 🔌 Circuits AC

| Function/Class | Description |
|----------------|-------------|
| `impedance_r(R: float) -> complex`| Converts a resistance value to its corresponding impedance value. |
| `impedance_l(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`L: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;` frequency: float \| None,`<br>&nbsp;&nbsp;&nbsp;&nbsp;` omega: float \| None`<br>`) -> complex`| Converts an inductance value to its corresponding impedance value. Supports both frequency and angular frequency. |
| `impedance_z(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`Z: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;` frequency: float \| None,`<br>&nbsp;&nbsp;&nbsp;&nbsp;` omega: float \| None`<br>`) -> complex`| Converts a capacitance value to its corresponding impedance value. Supports both frequency and angular frequency. |
| `series_impedance(*Z: float) -> complex` | Calculates the **total impedance** of impedances connected in **series**. |
| `parallel_impedance(*Z: float) -> complex` | Calculates the **total impedance** of impedances connected in **parallel**. |
| `phasor(magnitude: float, phase_deg: float) -> complex` | Converts magnitude and phase (degrees) to a complex phasor. |
| `to_polar(value: complex) -> dict[str, float]` | Convert a complex number to polar form. |
| `ac_power(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`voltage: float \| complex \| None,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`current: float \| complex \| None,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`values_are_rms: bool = True,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`phi_deg: float \| None,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`impedance: complex \| None,`<br>`)` | Calculates AC complex power. |
| `voltage_divider_ac(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`Vin: float \| complex,`<br>&nbsp;&nbsp;&nbsp;&nbsp;` Z1: complex,`<br>&nbsp;&nbsp;&nbsp;&nbsp;` Z2: complex`<br>`)` | Calculates the **voltage across Z1** in a two-impedance voltage divider. |
| `current_divider_ac(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`Iin: float \| complex,`<br>&nbsp;&nbsp;&nbsp;&nbsp;` Z1: complex,`<br>&nbsp;&nbsp;&nbsp;&nbsp;` Z2: complex`<br>`)` | Calculates the **current through Z1** in a two-branch current divider. |
| `mesh_current(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`equations: list[str],`<br>&nbsp;&nbsp;&nbsp;&nbsp;` variables: list[str], `<br>&nbsp;&nbsp;&nbsp;&nbsp;`decimals: int (default: 5)`<br>`)` | Solves for **mesh currents** symbolically using a system of equations. |
| `node_voltage(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`equations: list[str],`<br>&nbsp;&nbsp;&nbsp;&nbsp;` variables: list[str], `<br>&nbsp;&nbsp;&nbsp;&nbsp;`decimals: int (default: 5)`<br>`)` | Solves for **node voltages** symbolically using a system of equations. |
| `thevenin_from_voc_isc_ac(Voc: float, Isc: float)` | Builds a **Thevenin equivalent circuit** from open-circuit voltage (`Voc`) and short-circuit current (`Isc`). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.for_load(RL: float)` | Calculates **load voltage**, **current**, and **power** for a given load resistance `RL`. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.max_power()` | Computes the **load resistance (RL)** and **power** for **maximum power transfer**. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.to_norton()` | Converts a Thevenin equivalent to its **Norton equivalent**. |
| `norton_from_voc_isc_ac(Voc: float, Isc: float)` | Builds a **Norton equivalent circuit** from open-circuit voltage (`Voc`) and short-circuit current (`Isc`). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.for_load(RL: float)` | Calculates **load voltage**, **current**, and **power** for a given load resistance `RL`. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.max_power()` | Computes the **load resistance (RL)** and **power** for **maximum power transfer**. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.to_thevenin()` | Converts a Norton equivalent to its **Thevenin equivalent**. |

---

### 🧠 Digital Logic

| Function | Description |
|----------|-------------|
| `binary_to_decimal(binary_str: str)` | Converts a binary string to its decimal equivalent. |
| `decimal_to_binary(number: int)` | Converts a decimal integer to a binary string. |
| `binary_to_hexadecimal(binary_str: str)` | Converts a binary string to hexadecimal. |
| `hexadecimal_to_binary(hex_str: str)` | Converts a hexadecimal string to binary. |
| `decimal_to_twos_comp(number: int, bits: int)` | Converts a signed decimal integer to its two’s complement binary form using a specified number of bits. |
| `twos_comp_to_decimal(binary_str: str)` | Converts a two’s complement binary string to its decimal value. |
| `simplify_logic(expr: str)` | Simplifies Boolean expressions using **SymPy**’s logic simplifier. |
| `truth_table(expr: str, variables: list[str])` | Generates a Boolean truth table for a given logic expression and list of variables. |


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
| `half_wave_rectifier(`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`v_peak: float, `<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`diode_drop: float (default: 0.7),`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`show_plot: bool (default: False),`<br>`)` | Returns the idealized half-wave rectifier output metrics for sinusoidal input. Includes an option for outputting a plot of the output.  |
| `full_wave_rectifier(`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`v_peak: float, `<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`diode_drop: float (default: 0.7),`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`diode_drops_in_path: int (default: 2),`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`show_plot: bool (default: False),`<br>`)` | Return idealized full-wave rectifier output metrics for sinusoidal input. Includes an option for outputting a plot of the output. |
| `opamp_inverting_gain(`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`r_in: float, `<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`r_f: float,`<br>`)` | Calculates the ideal inverting amplifier gain. |
| `opamp_inverting_output(`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`v_in: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`r_in: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`r_f: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`, v_supply_pos: float \| None, `<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`v_supply_neg: float \| None,`<br>`)` | Calculates the output value of an ideal inverting amplifier for a given input voltage. |
| `opamp_nonverting_gain(`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`r_g: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`r_f: float,`<br>`)` | Calculates the ideal non-inverting amplifier gain. |
| `opamp_noninverting_output(`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`v_in: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`r_g: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`r_f: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`v_supply:pos: float \| None,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`v_supply_neg: float \| None,`<br>`)` | Calculates the output value of an ideal non-inverting amplifier for a given input voltage. |
| `opamp_summing_output(`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`inputs: list[float],`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`input_resistors: list[float],`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`r_f: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`v_supply_pos: float \| None,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`v_supply_neg: float \| None,`<br>`)` | Simplifies Boolean expressions using **SymPy**’s logic simplifier. |
| `opamp_differential_output(`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`v_plus: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`v_minus: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`r_in: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`r_f: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`v_supply_pos: float \| None,`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`v_supply_neg: float \| None,`<br>`)` | Calculates the output value of an ideal differential amplifier output with given input value. |

---

### 🌡️ Sensors

#### PT100 (RTD)

| Function | Description |
|----------|-------------|
| `pt100_resistance(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`temperature_celsius: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;` R0: float (default: 100.0),`<br>&nbsp;&nbsp;&nbsp;&nbsp;` A: float (default: 3.9083e-3),`<br>&nbsp;&nbsp;&nbsp;&nbsp;` B: float (default: -5.775e-7)`<br>`) -> str` | Calculates the resistance (Ω) of a PT100 RTD sensor for a given temperature in °C using the Callendar–Van Dusen equation. <br>**Defaults:** `R0=100.0`, `A=3.9083e-3`, `B=-5.775e-7`. <br>Returns a formatted string with the resistance and unit. Valid for 0–850 °C. |
| `pt100_temperature(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`resistance_ohms: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;` R0: float (default: 100.0),`<br>&nbsp;&nbsp;&nbsp;&nbsp;` A: float (default: 3.9083e-3),`<br>&nbsp;&nbsp;&nbsp;&nbsp;` B: float (default: -5.775e-7)`<br>`) -> str` | Calculates the temperature in °C from the resistance of a PT100 RTD sensor using the inverse Callendar–Van Dusen relation. <br>**Defaults:** `R0=100.0`, `A=3.9083e-3`, `B=-5.775e-7`. <br>Returns both quadratic solutions as formatted strings. Valid for 0–850 °C. |


#### Wheatstone Bridge

| Function | Description |
|----------|-------------|
| `wheatstone_voltage(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`R: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`R1: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`R2: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`R3: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`Vin: float`<br>`) -> float` | Calculates the **output voltage (Vout)** of a general Wheatstone bridge. <br>**Parameters:** `R` – sensor resistance (Ω), `R1`, `R2`, `R3` – known resistors (Ω), `Vin` – input voltage (V). <br>**Returns:** `Vout` in volts. |
| `wheatstone_balance_voltage(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`R: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`R1: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`Vin: float`<br>`) -> float` | Calculates the **output voltage (Vout)** of a balanced Wheatstone bridge where `R2 = R3`. <br>**Parameters:** `R` – sensor resistance (Ω), `R1` – known resistance (Ω), `Vin` – input voltage (V). <br>**Returns:** `Vout` in volts. |
| `wheatstone_resistance(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`Vout: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`R1: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`R2: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`R3: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`Vin: float`<br>`) -> float` | Calculates the **sensor resistance (R)** given the measured bridge output voltage. <br>**Parameters:** `Vout` – output voltage (V), `R1`, `R2`, `R3` – known resistors (Ω), `Vin` – input voltage (V). <br>**Returns:** `R` in ohms. |
| `wheatstone_balance_resistance(`<br>&nbsp;&nbsp;&nbsp;&nbsp;`R1: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`Vin: float,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`dV: float`<br>`) -> float` | Calculates the **sensor resistance (R)** in a balanced Wheatstone bridge given a small differential voltage. <br>**Parameters:** `R1` – known resistor (Ω), `Vin` – input voltage (V), `dV` – measured bridge voltage (V). <br>**Returns:** `R` in ohms. |

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
from sympy import symbols, Eq
from elektropy import node_voltage_dc, mesh_current_dc

V1, V2 = symbols("V1 V2")
print(node_voltage_dc([Eq(V1 + V2, 10), Eq(V1 - V2, 4)], ["V1", "V2"]))

I1, I2 = symbols("I1 I2")
print(mesh_current_dc([Eq(I1 + I2, 5), Eq(I1 - I2, 1)], ["I1", "I2"]))
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
print(voltage_divider_ac(100 + 0j, 10 + 5j, 20 - 5j))
print(current_divider_ac(10 + 0j, 10 + 5j, 20 - 5j))

p = phasor(10, 30)
print(p, to_polar(p))
print(ac_power(voltage=230, current=5, phi_deg=36.87))
print(ac_power(current=4 - 3j, impedance=36.8 + 27.6j))
```

### 🔄 Circuits AC: Node Voltage and Mesh Current

```python
from sympy import symbols, Eq
from elektropy import node_voltage_ac, mesh_current_ac

V1, V2 = symbols("V1 V2")
print(node_voltage_ac([Eq(V1 + V2, 3 - 1j), Eq(V1 - V2, 1 + 3j)], ["V1", "V2"]))

I1, I2 = symbols("I1 I2")
eqs = [Eq((1 + 1j) * I1 + I2, 1 + 2j), Eq(I1 + (2 - 1j) * I2, 4 - 2j)]
print(mesh_current_ac(eqs, ["I1", "I2"]))
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
    opamp_voltage_follower,
    opamp_summing_output,
    opamp_differential_output,
    opamp_integrator_output,
    opamp_differentiator_output,
    opamp_comparator,
)

print(opamp_inverting_gain(1000, 10000))
print(opamp_inverting_output(0.2, 1000, 10000))
print(opamp_noninverting_gain(1000, 9000))
print(opamp_noninverting_output(0.2, 1000, 9000))
print(opamp_voltage_follower(1.234))
print(opamp_summing_output([1.0, 0.5], [1000, 2000], 10000))
print(opamp_differential_output(1.2, 0.4, 1000, 10000))
print(opamp_integrator_output(1.0, 10000, 1e-6, 0.02))
print(opamp_differentiator_output(0.0, 1.0, 0.001, 10000, 1e-6))
print(opamp_comparator(2.0, 1.0, v_high=12.0, v_low=-12.0))
```

### 🔋 Analog Electronics: Rectifiers

```python
from elektropy import half_wave_rectifier, full_wave_rectifier

print(half_wave_rectifier(10.0, diode_drop=0.7))
print(full_wave_rectifier(10.0, diode_drop=0.7, diode_drops_in_path=2))

# Optional plots:
# half_wave_rectifier(10.0, diode_drop=0.7, show_plot=True)
# full_wave_rectifier(10.0, diode_drop=0.7, diode_drops_in_path=2, show_plot=True)
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
| PT100 out-of-range | Valid range: 0°C to 850°C |

---

## 👥 Contributors

- **Daniel Olsen** – Project author  
- **184446@stud.hvl.no** - Support

---

## 📄 License

MIT License – see the [LICENSE](LICENSE) file for full text.