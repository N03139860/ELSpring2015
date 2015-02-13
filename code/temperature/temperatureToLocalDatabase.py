#!/usr/bin/python
import temperature
import temperatureDatabase
import time

temperature = temperature.Temperature()
db = temperatureDatabase.TemperatureDatabase('../../misc/local.db')

while True:
  try:
    newMeasure = temperature.readTemp()
    db.dataEntry(newMeasure)
    print(newMeasure)
    time.sleep(900)
  except:
    print("Some error ocurred while reading temperature.")
    break

