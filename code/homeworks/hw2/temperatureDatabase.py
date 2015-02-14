#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

class TemperatureDatabase:

  def __init__(self, path_to_database):
    self.conn = sqlite3.connect(path_to_database)
    self.cur = self.conn.cursor()

  def dataEntry(self, data, tableName):
    with self.conn:
      self.cur.execute("INSERT INTO " + tableName + " (dateTime, celsiusTemperature, farenheitTemperature) VALUES( ?, ?, ?)", (data[0], data[1], data[2]))
      self.conn.commit()
      print(data)
