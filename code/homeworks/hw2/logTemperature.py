#!/usr/bin/python

import readTemp
import TemperatureDatabase

temperature = temperature.Temperature()
temperatureMeasurement = temperature.readTemp()

db = temperatureDatabase.TemperatureDatabase('../../misc/local.db')

db.dataEntry(temperatureMeasurement)

