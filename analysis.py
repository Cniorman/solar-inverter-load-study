"""Reproduces Table 4.2 and Figures 4.1-4.4 from data/inverter_readings.csv.
Run:  python analysis.py
"""
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("data/inverter_readings.csv")
v_nl = df.loc[df.load_percent == 0, "vout_V"].iloc[0]
d = df[df.load_percent > 0].copy()

d["pin_W"] = d.vin_V * d.iin_A                        # Eq 3.2
d["efficiency_%"] = d.pout_W / d.pin_W * 100          # Eq 3.3
d["power_loss_W"] = d.pin_W - d.pout_W
d["voltage_drop_%"] = (v_nl - d.vout_V) / d.vout_V * 100   # Eq 3.4
d["power_factor_check"] = d.pout_W / (d.vout_V * d.iout_A)  # Eq 3.5

table = d[["load_percent", "pin_W", "efficiency_%", "power_loss_W",
           "voltage_drop_%", "power_factor_check"]].round(2)
print(table.to_string(index=False))
table.to_csv("results/calculated_parameters.csv", index=False)

def plot(y, ylabel, name, marker="o"):
    plt.figure(figsize=(6, 4))
    plt.plot(d.load_percent, y, marker=marker, color="black")
    plt.xlabel("Load (% of rated capacity)")
    plt.ylabel(ylabel)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"results/{name}.png", dpi=200)
    plt.close()

plot(d["efficiency_%"], "Efficiency (%)", "fig4_1_efficiency")
plot(d.iout_A, "AC output current (A)", "fig4_3_output_current")
plot(d.temp_C, "Case temperature (°C)", "fig4_4_temperature", marker="D")

fig, ax1 = plt.subplots(figsize=(6, 4))
ax1.plot(d.load_percent, d.vin_V, "s-", color="black", label="DC input (left)")
ax1.set_xlabel("Load (% of rated capacity)")
ax1.set_ylabel("DC input voltage (V)")
ax2 = ax1.twinx()
ax2.plot(d.load_percent, d.vout_V, "^--", color="gray", label="AC output (right)")
ax2.set_ylabel("AC output voltage (V)")
fig.tight_layout()
fig.savefig("results/fig4_2_voltages.png", dpi=200)
print("\nVoltage regulation at 100% load: "
      f"{d.loc[d.load_percent == 100, 'voltage_drop_%'].iloc[0]:.2f} %")
