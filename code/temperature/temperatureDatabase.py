#!/usr/bin/python
import sqlite3

""" Log Current Time, Temperature in Celsius and Fahrenheit
    Prints a list [time, tempC, tempF] on a csv file """

class TemperatureDatabase:

  def __init__(self, path_to_database):
    self.conn = sqlite3.connect(path_to_database)
    self.cur = self.conn.cursor()

  def tableCreate(self, ):
    self.cur.execute("CREATE TABLE temperature(dateTime TEXT, celsiusTemperature TEXT, farenheitTemperature TEXT) ")

  def dataEntry(self, singleList):
    with self.conn:
      self.cur.execute("INSERT INTO temperature (dateTime, celsiusTemperature, farenheitTemperature) VALUES( ?, ?, ?)", (singleList[0], singleList[1], singleList[2]))
      self.conn.commit()