from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class Thevenin:
    Vth: float | complex
    Zth: float | complex

    def for_load(self, ZL: float | complex) -> Dict[str, float | complex]:
        """
        Return load voltage/current and power for a load ZL (ohms).
        """
        v_th = complex(self.Vth)
        z_th = complex(self.Zth)
        z_l = complex(ZL)
        z_total = z_th + z_l
        if z_total == 0:
            raise ValueError("Zth + ZL cannot be zero.")

        i_l = v_th / z_total
        v_l = i_l * z_l
        s_l = v_l * i_l.conjugate()
        return {"V_L": v_l, "I_L": i_l, "S_L": s_l, "P_L": s_l.real}

    def max_power(self) -> Dict[str, float | complex]:
        """
        Return optimal conjugate-matched load and maximum active power.
        """
        z_th = complex(self.Zth)
        z_l_opt = z_th.conjugate()
        p_max = abs(self.Vth) ** 2 / (4 * z_th.real) if z_th.real > 0 else 0.0
        return {"ZL_opt": z_l_opt, "Pmax": p_max}

    def to_norton(self) -> "Norton":
        """
        Convert to Norton: In = Vth/Zth, Zn = Zth.
        """
        z_th = complex(self.Zth)
        if z_th == 0:
            return Norton(In=float("inf"), Zn=0.0)
        return Norton(In=complex(self.Vth) / z_th, Zn=z_th)


def thevenin_from_voc_isc(Voc: float | complex, Isc: float | complex) -> Thevenin:
    """
    Build Thevenin from open-circuit voltage and short-circuit current.
    """
    i_sc = complex(Isc)
    if i_sc == 0:
        raise ValueError("Isc must be non-zero.")
    v_oc = complex(Voc)
    return Thevenin(Vth=v_oc, Zth=v_oc / i_sc)


@dataclass(frozen=True)
class Norton:
    In: float | complex
    Zn: float | complex

    def for_load(self, ZL: float | complex) -> Dict[str, float | complex]:
        """
        Return load voltage/current and power for a load ZL (ohms).
        """
        i_n = complex(self.In)
        z_n = complex(self.Zn)
        z_l = complex(ZL)
        z_total = z_n + z_l
        if z_total == 0:
            raise ValueError("Zn + ZL cannot be zero.")

        i_l = i_n * z_n / z_total
        v_l = i_l * z_l
        s_l = v_l * i_l.conjugate()
        return {"V_L": v_l, "I_L": i_l, "S_L": s_l, "P_L": s_l.real}

    def max_power(self) -> Dict[str, float | complex]:
        """
        Return optimal conjugate-matched load and maximum active power.
        """
        z_n = complex(self.Zn)
        z_l_opt = z_n.conjugate()
        p_max = abs(self.In) ** 2 * z_n.real / 4 if z_n.real > 0 else 0.0
        return {"ZL_opt": z_l_opt, "Pmax": p_max}

    def to_thevenin(self) -> Thevenin:
        """
        Convert to Thevenin: Vth = In*Zn, Zth = Zn.
        """
        z_n = complex(self.Zn)
        if z_n == 0:
            return Thevenin(Vth=float("inf"), Zth=0.0)
        return Thevenin(Vth=complex(self.In) * z_n, Zth=z_n)


def norton_from_voc_isc(Voc: float | complex, Isc: float | complex) -> Norton:
    """
    Build Norton from open-circuit voltage and short-circuit current.
    """
    i_sc = complex(Isc)
    if i_sc == 0:
        raise ValueError("Isc must be non-zero.")
    v_oc = complex(Voc)
    return Norton(In=i_sc, Zn=v_oc / i_sc)
