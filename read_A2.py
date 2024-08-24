import serial
import time

ser = serial.Serial('COM2', 9600) # Replace 'COM3' with your Arduino's serial port

while True:
    if ser.in_waiting:
        line = ser.readline().decode('utf-8').rstrip()
        if line == '1':
            print("I am Anik")
    time.sleep(1)
