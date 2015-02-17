#!/usr/bin/python
import temperature
import temperatureDatabase


temperature = temperature.Temperature()
db = temperatureDatabase.TemperatureDatabase('../../misc/local.db')

try:
  newMeasure = temperature.readTemp()
  db.dataEntry(newMeasure)
  print(newMeasure)
except:
  print("Some error ocurred while reading temperature.")

