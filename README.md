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

print(series_resistance(10, 20, 30))      # 60
print(pt100_temperature(138.5))           # Approx 100°C
print(simplify_logic("A*B' + A*B"))       # A
print(truth_table("A + B*C'", ["A", "B", "C"]))
```

---

## 🧩 Modules

All available functions in ElektroPy. Example usage is found below.

### 🔌 Circuits

| Function/Class | Description |
|----------------|-------------|
| `series_resistance(*R)` | Total resistance in series |
| `parallell_resistance(*R)` | Total resistance in parallel |
| `power_vi(V, I)` | Power using voltage and current |
| `power_ri(R, I)` | Power using resistance and current |
| `power_rv(R, V)` | Power using resistance and voltage |
| `voltage_divider(Vin, R1, R2)` | Voltage across R1 |
| `current_divider(Iin, R1, R2)` | Current through R1 |
| `mesh_current(equations, variables)` | Symbolic mesh current solver |
| `node_voltage(equations, variables)` | Symbolic node voltage solver |
| `thevenin_from_voc_isc(Voc, Isc)` | Build Thevenin from open/short |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.for_load(RL)` | Calculate load voltage, current, power for the given RL value |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.max_power()` | Calculates RL and the power for max power transfer |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.to_norton()` | Convert to Norton equivalent |
| `norton_from_voc_isc(Voc, Isc)` | Build Norton from open/short |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.for_load(RL)` | Calculate load voltage, current, power for the given RL value |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.max_power()` | Calculates RL and the power for max power transfer |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.to_thevenin()` | Convert to Thevenin equivalent |

---

### 🧠 Digital Logic

| Function | Description |
|----------|-------------|
| `binary_to_decimal(str)` | Convert binary to decimal |
| `decimal_to_binary(int)` | Convert decimal to binary |
| `binary_to_hexadecimal(str)` | Binary to hex |
| `hexadecimal_to_binary(str)` | Hex to binary |
| `decimal_to_twos_comp(int, bits)` | Decimal to 2's complement |
| `twos_comp_to_decimal(str)` | 2's complement to decimal |
| `simplify_logic(expr)` | Simplify Boolean expressions using SymPy |
| `truth_table(expr, variables)` | Generate a Boolean truth table |

---

### 🌡️ Sensors

#### PT100 (RTD)

| Function | Description |
|----------|-------------|
| `pt100_resistance(temp_C)` | PT100 resistance from temp |
| `pt100_temperature(res_ohms)` | Temperature from PT100 resistance |

#### Wheatstone Bridge

| Function | Description |
|----------|-------------|
| `wheatstone_voltage(R, R1, R2, R3, Vin)` | Output voltage of bridge |
| `wheatstone_balance_voltage(R, R1, Vin)` | Balance condition |
| `wheatstone_resistance(Vout, R1, R2, R3, Vin)` | Infer unknown resistance |
| `wheatstone_balance_resistance(R1, Vin, dV)` | Solve for R using balance voltage |

---

## 🧪 Examples

### Simplify Logic

```python
simplify_logic("A*B + A*B'")  # Output: A
```

### Generate a Truth Table

```python
print(truth_table("A + B*C'", ["A", "B", "C"]))
```

### Thevenin Equivalent

```python
th = thevenin_from_voc_isc(Voc=10, Isc=2)
print(th.for_load(10))  # {'V_L': ..., 'I_L': ..., 'P_L': ...}
```

### Mesh Current Method

```python
import sympy as sp
eqs = ["10 - 2*I1 - 2*(I1 - I2)", "2*(I2 - I1) + 3*I2"]
print(mesh_current(eqs, ["I1", "I2"]))
```

---

## 🧯 Troubleshooting

| Problem | Solution |
|---------|----------|
| `No solution found` | Check linear independence of equations |
| Logic errors | Ensure Boolean expressions use correct digital syntax: `'` = NOT, `*` = AND, `+` = OR, `~` = XOR |
| PT100 out-of-range | Valid range: 0°C to 850°C |

---

## 👥 Contributors

- **Daniel Olsen** – Project author  
- **184446@stud.hvl.no** - Support

---

## 📄 License

MIT License – see the [LICENSE](LICENSE) file for full text.