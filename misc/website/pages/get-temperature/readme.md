Get HHTP request from Raspberry pi Temperature Sensor

## 1. Cgi instalation in lighttpd
    ref: http://raspberrypi.stackexchange.com/questions/1346/how-to-get-python-to-work-with-lighttpd
    
    ### 1.1. Got the error: 
        [....] Reloading web server configuration: lighttpd2015-02-25 13:14:38: (plugin.c.169) dlopen() failed for: /usr/lib/lighttpd/mod_magnet.so /usr/lib/lighttpd/mod_magnet.so: cannot open shared object file: No such file or directory
        2015-02-25 13:14:38: (server.c.679) loading plugins finally failed
        
        #### Solved by installing mod-magnet
        ref: http://redmine.lighttpd.net/boards/2/topics/3854

## 2. Function getData fetches the last n measurements
