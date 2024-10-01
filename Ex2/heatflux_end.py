import matplotlib.pyplot as plt

# Data
x = [50, 100, 150, 200, 250, 300]
y = [(1445.2156+1445.1519)/2, 1109.4451, 771.415, 510.675, 330.78, (212.2971+212.289)/2]
y_T = [383.5, 362.2, 342, 325, 314.8, 306]

# Create figure and axis
fig, ax1 = plt.subplots()

# Plot y data on the left y-axis
ax1.plot(x, y, label='Heatflux at the end of the fin vs. lengths', color='tab:blue')
ax1.set_xlabel('Lengths (mm)')
ax1.set_ylabel('Heatflux (W/m^2)', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Create a second y-axis, sharing the same x-axis
ax2 = ax1.twinx()

# Plot y_T data on the right y-axis
ax2.plot(x, y_T, label='Temperature at the end of the fin vs. lengths', color='tab:red')
ax2.set_ylabel('Temperature (°C)', color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')

# Add title and grid
plt.title('Temperature and Heatflux over Fin Length')
plt.grid(True)

# Show the plot
plt.show()
