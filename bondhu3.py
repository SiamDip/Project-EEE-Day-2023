import serial.tools.list_ports
import serial
import time
import csv

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

# Open a CSV file to store the data
with open('arduino_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Start time
    start_time = time.time()
    while True:
        # Check if 30 seconds have passed
        if time.time() - start_time > 30:
            break

        if serialInst.in_waiting:
            packet = serialInst.readline().decode('utf').rstrip('\n')
            print(packet)
            writer.writerow([packet])

# Close the serial connection
serialInst.close()
