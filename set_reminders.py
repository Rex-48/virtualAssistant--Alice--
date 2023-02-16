import time
from datetime import date
import os

def reminder_write(path , data):
    file = open(path , "w")
    file.write(date.today()+" -- "+data)

def remider_read(path):
    os.startfile("D:/projects/virtualAssistant/remider.txt")