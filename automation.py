from pyfirmata import Arduino , util
import time

board = Arduino("COM3")

def switch_onn(pin1):
    board.digital[pin1].write(1)
    board.pass_time(1)


def switch_off(pin):
    board.digital[pin].write(0)
    board.pass_time(1)

