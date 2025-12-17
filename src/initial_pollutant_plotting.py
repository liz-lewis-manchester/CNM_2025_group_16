import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('/initial_conditions.csv', encoding = 'latin1')    #"latin1" was used to avoid special symbol

S = df["Distance (m)"].values
C = df["Concentration (µg/m_ )"].values

x = np.arange(0, 20, 0.2)   #create grid
C0 = np.interp(x, S, C)

print("x shape", x.shape)
print("C0 shape", C0.shape)

plt.figure()
plt.plot(x,C0)
plt.xlabel("Distance x (m)")
plt.ylabel("Concentration C (µg/m³)")
plt.title("Initial pollutant concentration")
plt.grid(True)            #use grid for easiler reading
plt.show()
