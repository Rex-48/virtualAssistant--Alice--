from pyfirmata import Arduino , util
import time

board = Arduino("COM3")

def switch1(pin1):
    board.digital[pin1].write(1)
    board.pass_time(1)


def switch2(pin1,pin2):
    board.digital[pin1].write(1)
    board.pass_time(1)
    board.digital[pin2].write(1)
    board.pass_time(1)


def switch3(pin1,pin2,pin3):
    
    board.digital[pin1].write(1)
    board.pass_time(1)
    
    board.digital[pin2].write(1)
    board.pass_time(1)
    
    board.digital[pin3].write(1)
    board.pass_time(1)


def switch4(pin1,pin2,pin3,pin4):
    
    board.digital[pin1].write(1)
    board.pass_time(1)
    
    board.digital[pin2].write(1)
    board.pass_time(1)
    
    board.digital[pin3].write(1)
    board.pass_time(1)
    
    board.digital[pin4].write(1)
    board.pass_time(1)




switch1(2)
switch2(2,3)
switch3(3,4,5)
switch4(2,3,4,5)