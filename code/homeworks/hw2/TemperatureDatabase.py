#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

class TemperatureDatabase:

  def __init__(self, path_to_database):
    self.conn = sqlite3.connect(path_to_database)
    self.cur = self.conn.cursor()

  def dataEntry(self, singleList):
    with self.conn:
      self.cur.execute("INSERT INTO temperature (dateTime, celsiusTemperature, farenheitTemperature) VALUES( ?, ?, ?)", (singleList[0], singleList[1], singleList[2]))
      self.conn.commit()
