import serial
import time

arduino = serial.Serial('/dev/tty.usbmodem14101', 9600)


def quitaCaracter(temperatura):
    return str(temperatura).replace("b'", "").replace("\\r\\n'", "")


def getMedicion():
    rawString = arduino.readline()
    return quitaCaracter(rawString)


def cerrarSerial():
    arduino.close()