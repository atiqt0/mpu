import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Load the data from the CSV file
data = pd.read_csv('gyro1.csv', delim_whitespace=True, header=None, names=['time', 'ax', 'ay', 'az', 'gx', 'gy', 'gz'])

# Display the first few rows of the dataframe
print(data.head())

# Define the number of recent data points to display
trail_length = 20

# Create a figure and axis for accelerometer data
fig1, ax1 = plt.subplots()
accel_line, = ax1.plot([], [], 'b-', label='Accelerometer')
accel_text = ax1.text(0.02, 0.95, '', transform=ax1.transAxes)

# Set the limits of the plot for accelerometer data
ax1.set_xlim(data['ax'].min(), data['ax'].max())
ax1.set_ylim(data['ay'].min(), data['ay'].max())

# Set labels for accelerometer data
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.legend()

# Initialize the plot for accelerometer data
def init_accel():
    accel_line.set_data([], [])
    accel_text.set_text('')
    return accel_line, accel_text

# Update the plot for each frame for accelerometer data
def update_accel(frame):
    start = max(0, frame - trail_length)
    accel_line.set_data(data['ax'][start:frame], data['ay'][start:frame])
    accel_text.set_text(f'Frame: {frame}\nX: {data["ax"][frame]:.2f}, Y: {data["ay"][frame]:.2f}, Z: {data["az"][frame]:.2f}')
    return accel_line, accel_text

# Create the animation for accelerometer data
ani_accel = animation.FuncAnimation(fig1, update_accel, frames=len(data), init_func=init_accel, blit=True, interval=100)

# Create a figure and axis for gyroscope data
fig2, ax2 = plt.subplots()
gyro_line, = ax2.plot([], [], 'r-', label='Gyroscope')
gyro_text = ax2.text(0.02, 0.95, '', transform=ax2.transAxes)

# Set the limits of the plot for gyroscope data
ax2.set_xlim(data['gx'].min(), data['gx'].max())
ax2.set_ylim(data['gy'].min(), data['gy'].max())

# Set labels for gyroscope data
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.legend()

# Initialize the plot for gyroscope data
def init_gyro():
    gyro_line.set_data([], [])
    gyro_text.set_text('')
    return gyro_line, gyro_text

# Update the plot for each frame for gyroscope data
def update_gyro(frame):
    start = max(0, frame - trail_length)
    gyro_line.set_data(data['gx'][start:frame], data['gy'][start:frame])
    gyro_text.set_text(f'Frame: {frame}\nX: {data["gx"][frame]:.2f}, Y: {data["gy"][frame]:.2f}, Z: {data["gz"][frame]:.2f}')
    return gyro_line, gyro_text

# Create the animation for gyroscope data
ani_gyro = animation.FuncAnimation(fig2, update_gyro, frames=len(data), init_func=init_gyro, blit=True, interval=100)

# Create a figure and axis for displaying current data
fig3, ax3 = plt.subplots()
current_text = ax3.text(0.5, 0.5, '', transform=ax3.transAxes, ha='center', va='center', fontsize=12)
ax3.axis('off')  # Hide the axes

# Initialize the plot for current data
def init_current():
    current_text.set_text('')
    return current_text,

# Update the plot for each frame for current data
def update_current(frame):
    current_text.set_text(f'Frame: {frame}\n'
                          f'Accelerometer:\nX: {data["ax"][frame]:.2f}, Y: {data["ay"][frame]:.2f}, Z: {data["az"][frame]:.2f}\n'
                          f'Gyroscope:\nX: {data["gx"][frame]:.2f}, Y: {data["gy"][frame]:.2f}, Z: {data["gz"][frame]:.2f}')
    return current_text,

# Create the animation for current data
ani_current = animation.FuncAnimation(fig3, update_current, frames=len(data), init_func=init_current, blit=True, interval=100)

# Show the plots
plt.show()