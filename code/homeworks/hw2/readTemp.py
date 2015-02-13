#!/usr/bin/python
import os
import time
import csv

""" Log Current Time, Temperature in Celsius and Fahrenheit    
Returns a list [time, tempC, tempF] """

class Temperature(object):

  def readTemp(self):
    tempfile = open("/sys/bus/w1/devices/28-0000069647a3/w1_slave")
    tempfile_text = tempfile.read()
    currentTime=time.strftime('%x %X %Z')
    tempfile.close()
    tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
    tempF=tempC*9.0/5.0+32.0
    return [currentTime, tempC, tempF]

print readTemp() 