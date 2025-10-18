# rpu_core/twa_demo/run_twa_demo.py
# Квази-TWA демо: уравнения Блоха со связным драйвом и затуханием.
# Пишем траектории <σz>(t) для разных γ/Ω, как в картах из PRX-типа работ.

import numpy as np
from dataclasses import dataclass
from pathlib import Path
import csv
import time

@dataclass
class Params:
    Omega: float      # частота когерентного драйва (рад/с, но единицы относительные)
    gamma: float      # скорость затухания (1/с, относительные)
    delta: float      # расстройка (Δ = ω0 - ωdrive)
    T: float          # конечное время моделирования
    dt: float         # шаг интегрирования
    s0: np.ndarray    # начальный вектор спина [sx, sy, sz]

def rk4_step(f, y, t, h, args):
    k1 = f(t, y, *args)
    k2 = f(t + 0.5*h, y + 0.5*h*k1, *args)
    k3 = f(t + 0.5*h, y + 0.5*h*k2, *args)
    k4 = f(t + h,     y + h*k3,     *args)
    return y + (h/6.0)*(k1 + 2*k2 + 2*k3 + k4)

def bloch_rhs(t, s, Omega, gamma, delta):
    sx, sy, sz = s
    # Уравнения Блоха с продольным затуханием к равновесию sz_eq = -1 (основное состояние)
    # и поперечным затуханием ~gamma/2 (минимально прилично, без занудства).
    T1 = 1.0/max(gamma, 1e-12)
    T2 = 2.0*T1

    dsx = -sx/T2 + delta*sy
    dsy = -sy/T2 - delta*sx + Omega*sz
    dsz = -(sz + 1.0)/T1 - Omega*sy
    return np.array([dsx, dsy, dsz])

def run(params: Params, out_csv: Path):
    t = 0.0
    s = params.s0.astype(float).copy()
    steps = int(params.T/params.dt)

    out_csv.parent.mkdir(parents=True, exist_ok=True)
    with out_csv.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["t", "sx", "sy", "sz"])
        for _ in range(steps+1):
            w.writerow([t, s[0], s[1], s[2]])
            s = rk4_step(bloch_rhs, s, t, params.dt,
                         args=(params.Omega, params.gamma, params.delta))
            t += params.dt

def main():
    # Нормируем время в единицах 1/Ω для удобства сравнения
    Omega = 1.0  # задаём за эталон
    gammas = [0.1, 0.2, 0.5, 1.0]  # относительные γ/Ω
    delta = 0.0
    periods = 20.0    # «Qt» на картинках: до 20 периодов
    dt = 0.0025       # достаточно мелко для RK4
    T = periods*(2*np.pi/Omega)

    logs_dir = Path(__file__).parent / "logs"
    stamp = time.strftime("%Y%m%d_%H%M%S")

    s0 = np.array([0.0, 0.0, -1.0])  # начинаем в основном состоянии

    for g_rel in gammas:
        params = Params(Omega=Omega, gamma=g_rel*Omega, delta=delta,
                        T=T, dt=dt, s0=s0)
        out_csv = logs_dir / f"bloch_Omega{Omega:g}_gammaOverOmega{g_rel}_stamp{stamp}.csv"
        run(params, out_csv)
        print(f"[ok] written {out_csv}")

if __name__ == "__main__":
    main()
