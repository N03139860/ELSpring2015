#!/usr/bin/python
import temperature
import temperatureDatabase


temperature = temperature.Temperature()
db = temperatureDatabase.TemperatureDatabase('../../misc/local.db')

try:
  newMeasure = temperature.readTemp()
  db.dataEntry(newMeasure)
  print(newMeasure)
  farenheitTemperature = float(newMeasure[2])
  if farenheitTemperature > 80.0:
  	gmail_from_pi_post.Email().sendEmail(newMeasure)
	print("Email sent")
except:
  print("Some error ocurred while reading temperature.")

