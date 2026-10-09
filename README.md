# Performance Evaluation of a Solar Inverter under Variable Load Conditions

Experimental study of how the efficiency, output voltage, current, power factor and temperature of a 1000 W solar inverter change with load (20%–100% of rated capacity).

**Author:** Usman Idris Bala
**Supervisor:** Prof. Aminu Saidu, Department of Physics, Usmanu Danfodiyo University, Sokoto
**Report:** B.Sc. Physics project, October 2026 → [`paper/Solar_Inverter_Project_Full_Report.pdf`](Solar_Inverter_Project_Full_Report.pdf)

## What was done
A single-phase 1000 W inverter, powered from a 12 V deep-cycle battery, was loaded with a resistive load bank at 20, 40, 60, 80 and 100% of rated capacity. At each level the DC input voltage and current, AC output voltage, current and power, power factor and case temperature were recorded (mean of three repeated runs).

## Main results (inverter tested)
| Load | Efficiency | Power loss | Voltage drop |
|---|---|---|---|
| 20% | 82.0% | 43.9 W | 0.65% |
| 40% | 90.0% | 44.4 W | 0.96% |
| 60% | 93.0% | 45.1 W | 1.35% |
| 80% | 92.0% | 69.6 W | 1.93% |
| 100% | 89.0% | 123.6 W | 2.75% |

- Efficiency is lowest at light load, peaks at 60% load, and falls near full load, so one peak-efficiency figure does not describe real performance.
- Power loss is almost constant (44–45 W) up to 60% load, then rises sharply.
- Voltage regulation is 2.75%; power factor stays at 0.99–1.00; case temperature rises from 31 °C to 53 °C.
- For this unit, running at about 40–80% of rated load gave efficiency of 90% or higher.

## Repository contents
```
paper/Solar_Inverter_Project_Full_Report.pdf   full project report
data/inverter_readings.csv                     mean readings (Table 4.1)
analysis.py                                    reproduces Table 4.2 and Figures 4.1–4.4
results/                                       calculated table and figures
requirements.txt                               Python packages
```

## Reproduce the results
```
pip install -r requirements.txt
python analysis.py
```

## Limitations
One inverter only, resistive loads only, short tests, loads applied in ascending order (heating and battery drain accumulate), and no statistical test on the individual readings. Conclusions apply to the inverter tested. See Sections 1.8 and 3.11 of the report.

## Licence
MIT, see `LICENSE`.
