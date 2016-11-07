# coding=UTF-8

import time
import serial


ptn = [0xAA,0x50,0x60,0x70] 

def main():
    
    ser = serial.Serial('COM3', 2400, timeout=0.5)
    ary = bytearray(ptn)
    ser.write(ary)
    time.sleep(0.1)
    ser.close()    




