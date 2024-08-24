import serial.tools.list_ports
import serial
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import datetime

# List all available ports
ports = serial.tools.list_ports.comports()
portsList = []

for onePort in ports:
    portsList.append(str(onePort))
    print(str(onePort))

val = input("Select Port: COM")

# Determine the selected port
for x in range(0, len(portsList)):
    if portsList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portVar)

# Setup the serial connection
serialInst = serial.Serial()
serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()

# Set up the plot
fig, ax = plt.subplots()
times = deque(maxlen=100)  # deque to hold the latest 100 timestamps
values = deque(maxlen=100)  # deque to hold the latest 100 data points
line, = ax.plot([], [], lw=2)

# Initialize the plot
def init():
    ax.set_ylim(470, 550)  # Adjust y-axis limits based on your data range
    ax.set_xlim(datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(seconds=10))  # Adjust as needed
    return line,

# Update function for the animation
def update(frame):
    if serialInst.in_waiting:
        packet = serialInst.readline().decode('utf').rstrip('\n')
        try:
            data_point = int(packet)
            current_time = datetime.datetime.now()
            times.append(current_time)
            values.append(data_point)
            line.set_data(times, values)
            ax.set_xlim(times[0], current_time + datetime.timedelta(seconds=1))  # Adjust as needed
        except ValueError:
            pass  # Handle the case where the packet is not a valid integer
    return line,

# Animation with save_count
ani = animation.FuncAnimation(fig, update, init_func=init, blit=True, save_count=200)

plt.show()

# Close the serial connection (won't be reached if window is closed)
serialInst.close()
