import time
from datetime import date
import os

def reminder_write(path , data):
    file = open(path , "w")
    tdate = str(date.today())
    file.write(tdate+" -- "+data)

def reminder_read(path):
    os.startfile(path)

