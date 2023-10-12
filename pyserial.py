import serial
import time
import sys

param = sys.argv[1]

ser1 = serial.Serial("COM6", baudrate=9600) # ser1 = rail
ser2 = serial.Serial("COM7", baudrate=9600) # ser2 = compressor
ser3 = serial.Serial("COM8", baudrate=9600) # ser3 = GMotor
time.sleep(2)

if param == '3.0': # general trash
    ser1.write('1\n'.encode()) # rail run
    ser3.write('start'.encode()) # GMotor start

elif param == '1.0' or param == '2.0': # plastic trash
    ser2.write('compress\n'.encode()) # compressor run
    ser1.write('2\n'.encode()) # rail run
    time.sleep(32) # wait for 32 seconds
    ser3.write('start'.encode()) # GMotor start

elif param == '0.0': # can
    ser2.write('compress\n'.encode()) # compressor run
    ser1.write('3\n'.encode()) # rail run
    time.sleep(64) # wait for 64 seconds
    ser3.write('start'.encode()) # GMotor start

ser1.close()
ser2.close()
ser3.close()
