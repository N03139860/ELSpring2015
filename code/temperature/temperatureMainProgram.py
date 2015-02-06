#!/usr/bin/python
import temperature
import temperatureDatabase

temperature = temperature.Temperature()
listOfTemperatures = temperature.getListOfTemperatures(20, 0.001)

db = temperatureDatabase.TemperatureDatabase('../misc/local.db')

for list in listOfTemperatures:
  db.dataEntry(list)
