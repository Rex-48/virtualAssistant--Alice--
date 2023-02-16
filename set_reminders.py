import time
from datetime import date
import os

def reminder_write(path , data):
    file = open(path , "w")
    file.write(date.today()+" -- "+data)

def reminder_read(path):
    os.startfile(path)

