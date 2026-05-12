import serial
import serial.tools.list_ports
import pandas as pd

ports = list(serial.tools.list_ports.comports())
currentPort = ""

# Find the port that the arduino is connected to
for p in ports:
    if "n/a" not in p:
        currentPort = p.device


ardiuno = serial.Serial(currentPort, 9600)
print(f"Connected to {currentPort}")

while ardiuno.readline() is not None:
    print(ardiuno.readline())

