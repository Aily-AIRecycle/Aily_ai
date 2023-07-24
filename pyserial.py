import serial
import time
import sys

param = sys.argv[1]

ser1 = serial.Serial("COM6", baudrate=9600) # ser1 = rail
ser2 = serial.Serial("COM7", baudrate=9600) # ser2 = compressor

time.sleep(2)

ser2.write('compress\n'.encode()) # comspressor run


if param == '3.0': # general trash
    ser1.write('1\n'.encode()) # rail run
if param == '1.0' or '2.0': # plastic trash
    ser1.write('2\n'.encode()) # rail run
if param == '0.0': # can
    ser1.write('3\n'.encode()) # rail run


ser1.close()
ser2.close()