import matplotlib.pyplot as plt
import numpy as np
import csv
from pathlib import Path

def load_csv(file_path):
    t, sx, sy, sz = [], [], [], []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            t.append(float(row['t']))
            sx.append(float(row['sx']))
            sy.append(float(row['sy']))
            sz.append(float(row['sz']))
    return np.array(t), np.array(sx), np.array(sy), np.array(sz)

def plot_results(files):
    plt.figure(figsize=(10, 6))
    for f in files:
        t, sx, sy, sz = load_csv(f)
        label = Path(f).stem
        plt.plot(t, sz, label=label)
    plt.xlabel("Ωt")
    plt.ylabel("⟨σz⟩")
    plt.title("Bloch Dynamics — TWA Simulation")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    logs_dir = Path(__file__).parent / "logs"
    files = sorted(logs_dir.glob("*.csv"))
    if not files:
        print("Нет данных для отображения. Сначала запусти run_twa_demo.py")
    else:
        plot_results(files)
