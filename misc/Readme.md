A directory for miscellaneous stuff of N03139860.

## Homework 3
HW3 may be found in the directory cgi-bin/get-temperature
link: http://kikocastro.ddns.net/cgi-bin/get-temperature/getTemperature.py?timeinterval=200

### Description:

1) Cgi module was installed to be used with lighttpd 
reference: https://mike632t.wordpress.com/2013/09/21/installing-lighttpd-with-python-cgi-support/

2) The method getData.get_data() fetches the lastXMinutes/5 (5 is the refreshing interval) rows

3) The file getTemperature.py is responsible to build the html interface and fetching the data from get_data() based on the GET request
reference: http://raspberrywebserver.com/cgiscripting/rpi-temperature-logger/building-a-web-user-interface-for-the-temperature-monitor.html


