#!/usr/bin/python

# get data from the database
# if an interval in minutes (integer)  is passed,
# return a list of records from the database for the last X minutes

import sqlite3
import os
import datetime

dir_path = os.path.dirname(os.path.abspath(__file__))

def get_data(path_to_database, lastXMinutes):

  conn = sqlite3.connect(os.path.join(dir_path, path_to_database))
  cur = conn.cursor()

  if lastXMinutes == None:
    cur.execute("SELECT * FROM temperature DESC LIMIT 300")
  else:
    # cur.execute("SELECT * FROM temperature WHERE datetime(dateTime)>datetime('now','-%s minutes')" % lastXMinutes)
    cur.execute("SELECT * FROM temperature ORDER BY dateTime  DESC LIMIT ?",  (str(lastXMinutes/5),))


  rows=cur.fetchall()

  conn.close()

  return rows


# original code from http://raspberrywebserver.com/cgiscripting/rpi-temperature-logger/building-a-web-user-interface-for-the-temperature-monitor.html

