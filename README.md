# ⚡ ElektroPy: Electronics and Digital Logic Toolkit

**ElektroPy** is a Python library for electrical engineering education and analysis. It covers basic circuit theory, sensor simulation (PT100, Wheatstone), and digital logic (truth tables, logic simplification, binary systems). Ideal for students, educators, and engineers alike.

---

## 📚 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Modules](#-modules)
  - [Circuits](#circuits)
  - [Digital Logic](#digital-logic)
  - [Sensors](#sensors)
- [Examples](#-examples)
- [Troubleshooting](#-troubleshooting)
- [Contributors](#-contributors)
- [License](#-license)

---

## ✨ Features

- 📐 **Circuit analysis**: Mesh current and node voltage solvers
- 🔋 **Power computations**: VI, RV, and RI based power
- ⚙️ **Component modeling**: Thevenin/Norton equivalents
- 🔧 **Sensor simulations**: PT100 RTD and Wheatstone bridge
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

### 🔌 Circuits

| Function/Class | Description |
|----------------|-------------|
| `series_resistance(*R: float)` | Calculates the **total resistance** of resistors connected in **series**. |
| `parallel_resistance(*R: float)` | Calculates the **total resistance** of resistors connected in **parallel**. |
| `power_vi(V: float, I: float)` | Computes **power (W)** using voltage and current: *P = V × I*. |
| `power_ri(R: float, I: float)` | Computes **power (W)** using resistance and current: *P = I² × R*. |
| `power_rv(R: float, V: float)` | Computes **power (W)** using resistance and voltage: *P = V² / R*. |
| `voltage_divider(Vin: float, R1: float, R2: float)` | Calculates the **voltage across R1** in a two-resistor voltage divider. |
| `current_divider(Iin: float, R1: float, R2: float)` | Calculates the **current through R1** in a two-branch current divider. |
| `mesh_current(equations: list[str], variables: list[str])` | Solves for **mesh currents** symbolically using a system of equations. |
| `node_voltage(equations: list[str], variables: list[str])` | Solves for **node voltages** symbolically using a system of equations. |
| `thevenin_from_voc_isc(Voc: float, Isc: float)` | Builds a **Thevenin equivalent circuit** from open-circuit voltage (`Voc`) and short-circuit current (`Isc`). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.for_load(RL: float)` | Calculates **load voltage**, **current**, and **power** for a given load resistance `RL`. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.max_power()` | Computes the **load resistance (RL)** and **power** for **maximum power transfer**. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.to_norton()` | Converts a Thevenin equivalent to its **Norton equivalent**. |
| `norton_from_voc_isc(Voc: float, Isc: float)` | Builds a **Norton equivalent circuit** from open-circuit voltage (`Voc`) and short-circuit current (`Isc`). |
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

### 🌡️ Sensors

#### PT100 (RTD)

| Function | Description |
|----------|-------------|
| `pt100_resistance(temperature_celsius: float, R0: float = 100.0, A: float = 3.9083e-3, B: float = -5.775e-7)` | Calculates the resistance (Ω) of a PT100 RTD sensor for a given temperature in °C using the Callendar–Van Dusen equation. <br>**Defaults:** `R0=100.0`, `A=3.9083e-3`, `B=-5.775e-7`. <br>Returns a formatted string with the resistance and unit. Valid for 0–850 °C. |
| `pt100_temperature(resistance_ohms: float, R0: float = 100.0, A: float = 3.9083e-3, B: float = -5.775e-7)` | Calculates the temperature in °C from the resistance of a PT100 RTD sensor using the inverse Callendar–Van Dusen relation. <br>**Defaults:** `R0=100.0`, `A=3.9083e-3`, `B=-5.775e-7`. <br>Returns both quadratic solutions as formatted strings. Valid for 0–850 °C. |


#### Wheatstone Bridge

| Function | Description |
|----------|-------------|
| `wheatstone_voltage(R, R1, R2, R3, Vin)` | Calculates the **output voltage (Vout)** of a general Wheatstone bridge. <br>**Parameters:** `R` – sensor resistance (Ω), `R1`, `R2`, `R3` – known resistors (Ω), `Vin` – input voltage (V). <br>**Returns:** `Vout` in volts. |
| `wheatstone_balance_voltage(R, R1, Vin)` | Calculates the **output voltage (Vout)** of a balanced Wheatstone bridge where `R2 = R3`. <br>**Parameters:** `R` – sensor resistance (Ω), `R1` – known resistance (Ω), `Vin` – input voltage (V). <br>**Returns:** `Vout` in volts. |
| `wheatstone_resistance(Vout, R1, R2, R3, Vin)` | Calculates the **sensor resistance (R)** given the measured bridge output voltage. <br>**Parameters:** `Vout` – output voltage (V), `R1`, `R2`, `R3` – known resistors (Ω), `Vin` – input voltage (V). <br>**Returns:** `R` in ohms. |
| `wheatstone_balance_resistance(R1, Vin, dV)` | Calculates the **sensor resistance (R)** in a balanced Wheatstone bridge given a small differential voltage. <br>**Parameters:** `R1` – known resistor (Ω), `Vin` – input voltage (V), `dV` – measured bridge voltage (V). <br>**Returns:** `R` in ohms. |

---

## 🧪 Examples

### Simplify logic

```python
simplify_logic("A*B + A*B!")  # Output: A
```

### Generate a truth table

```python
print(truth_table("A + B*C'", ["A", "B", "C"]))
```

### Convert between number systems

```python
print(binary_to_decimal("1101"))      # 13
print(decimal_to_binary(13))          # "1101"
print(decimal_to_twos_comp(-5, 8))    # "11111011"
print(twos_comp_to_decimal("11111011"))  # -5
```

### Norton equivalent

```python
nt = norton_from_voc_isc(Voc=10, Isc=2)
print(nt.for_load(10))
# {'V_L': 5.0, 'I_L': 0.5, 'P_L': 2.5}
```

### Mesh current method

```python
import sympy as sp
eqs = ["10 - 2*I1 - 2*(I1 - I2)", "2*(I2 - I1) + 3*I2"]
print(mesh_current(eqs, ["I1", "I2"]))
```

### Series and parallell resistance

```python
print(series_resistance(10, 20, 30))   # 60 Ω
print(parallel_resistance(100, 200))   # 66.67 Ω
```

### Voltage and power calculations

```python
print(voltage_divider(12, 4, 8))  # 4.0 V
print(power_vi(12, 0.5))          # 6.0 W
```

### PT100 (RTD)

```python
print(pt100_resistance(100))      # "138.505 Ω"
print(pt100_temperature(138.5))   # {'Solution 1: 100.003 ℃ ', 'Solution 2: -389.529 ℃ '}
```

### Wheatstone bridge

```python
print(wheatstone_voltage(120, 100, 100, 100, 5))     # 0.2083 V
print(wheatstone_balance_voltage(102, 100, 5))       # 0.0245 V
print(wheatstone_resistance(0.1, 100, 100, 100, 5))  # 102.15 Ω
print(wheatstone_balance_resistance(100, 5, 0.02))   # 104.26 Ω
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