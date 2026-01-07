import pandas as pd
import matplotlib.pyplot as plt

import schemdraw
import schemdraw.elements as elm

# Test Circuit Diagram

with schemdraw.Drawing() as d:
    
    d += (V1 := elm.SourceV().label('VDC').up())
    d += elm.Resistor().right().label('$R_s$')
    d += (A1 := elm.MeterA().right().label('Iz'))
    d += elm.Line().down().length(3)
    d += (Z1 := elm.Zener().up().label('PZU15B3', loc='bottom'))
    d += elm.Line().down().length(1)
    d += elm.Line().right().at(Z1.start).length(3)
    d += elm.MeterV().up().label('Vz', loc='bottom')
    d += elm.Line().left().length(3)
    d += elm.Line().down().length(3)
    d += elm.Line().to(V1.start)
    d += elm.Ground().at(V1.start)
    d.draw()

# Graph plotting

data = pd.read_csv('measurements.csv')

plt.figure(figsize=(16, 6))
plt.style.use('seaborn-v0_8-whitegrid')

plt.subplot(1, 2, 1)
plt.plot(data['V_DC'], data['I_25C'], label='25°C', linewidth=2)
plt.plot(data['V_DC'], data['I_50C'], label='50°C', linewidth=2)
plt.plot(data['V_DC'], data['I_100C'], label='100°C', linewidth=2)
plt.plot(data['V_DC'], data['I_150C'], label='150°C', linewidth=2)
plt.plot(data['V_DC'], data['I_-30C'], label='-30°C', linewidth=2)

plt.title('PZU15B3 Current Curves', fontsize=14)
plt.xlabel('Voltage (V)', fontsize=12, fontweight='bold')
plt.ylabel('Leak Current (mA)', fontsize=12, fontweight='bold')
plt.legend(title="Temperature")
plt.grid(True, which="both", ls="-", alpha=0.5)

plt.subplot(1, 2, 2)
plt.plot(data['V_DC'], data['V_25C'], label='25°C', linewidth=2)
plt.plot(data['V_DC'], data['V_50C'], label='50°C', linewidth=2)
plt.plot(data['V_DC'], data['V_100C'], label='100°C', linewidth=2)
plt.plot(data['V_DC'], data['V_150C'], label='150°C', linewidth=2)
plt.plot(data['V_DC'], data['V_-30C'], label='-30°C', linewidth=2)

plt.title('PZU15B3 Zener Voltage Curves', fontsize=14)
plt.xlabel('Voltage (V)', fontsize=12, fontweight='bold')
plt.ylabel('Zener Voltage (V)', fontsize=12, fontweight='bold')
plt.legend(title="Temperature")
plt.grid(True, which="both", ls="-", alpha=0.5)

plt.show()
print("Zener Diode Characteristic Curves Plotted")

