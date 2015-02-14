#!/usr/bin/python

import readTemp
import temperatureDatabase

temperature = readTemp.Temperature()
newMeasurement = temperature.readTemp()

db = temperatureDatabase.TemperatureDatabase('../../../misc/temperature.db')
db.dataEntry(newMeasurement, 'TempData')