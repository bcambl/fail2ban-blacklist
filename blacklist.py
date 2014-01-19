#!/usr/bin/python

from sys import argv
import re


ip = argv[1]
val = re.compile("^0*([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.0*([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.0*([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.0*([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])$")
valip = val.match(ip)
found = 0
if valip:
    print "is valid"
    f = open("/etc/fail2ban/ip.blacklist", "r")
    for i in f:
        if ip in i:
            found = 1
    f.close()
    if found == 0:
        f = open("/etc/fail2ban/ip.blacklist", "a")
        f.write(ip)
        f.close()
else:
    pass
