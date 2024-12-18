from threading import Thread
from scripts import *
from assets import *

def main():
    GPS_Thread = Thread(gps.main())
    GPS_Thread.start()
    GPS_Thread.join
