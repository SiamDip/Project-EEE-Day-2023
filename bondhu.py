import serial
import time

# Replace 'COM3' with the port where your Arduino is connected
arduino = serial.Serial('COM2', 9600, timeout=1)
time.sleep(2)  # Give the connection a second to settle

try:
    while True:
        if arduino.in_waiting > 0:
            line = arduino.readline().decode('utf-8').rstrip()
            print(line)
            # You can process your data here
except KeyboardInterrupt:
    print("Data collection stopped")
    arduino.close()
