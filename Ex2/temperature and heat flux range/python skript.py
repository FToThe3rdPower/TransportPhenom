import pandas as pd
import matplotlib.pyplot as plt

# Data from the given table
data = {
    "end_of_fin_m": [0.05, 0.1, 0.15, 0.2, 0.25, 0.3],
    "T_k": [383.5, 362.2, 342, 325, 314.8, 306],
    "HF_W_m2": [1500, 1000, 2000, 0, 0, 0]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create the plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plotting Temperature (T) vs end of fin
ax1.set_xlabel('End of Fin (m)')
ax1.set_ylabel('Temperature (K)', color='tab:blue')
ax1.plot(df['end_of_fin_m'], df['T_k'], marker='o', color='tab:blue', label='Temperature (K)')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Create a second y-axis to plot Heat Flux (HF)
ax2 = ax1.twinx()
ax2.set_ylabel('Heat Flux (W/m²)', color='tab:red')
ax2.plot(df['end_of_fin_m'], df['HF_W_m2'], marker='o', color='tab:red', label='Heat Flux (W/m²)')
ax2.tick_params(axis='y', labelcolor='tab:red')

# Title and grid
plt.title('Temperature and Heat Flux vs End of Fin')
ax1.grid()
fig.tight_layout()

# Show the plot
plt.show()
