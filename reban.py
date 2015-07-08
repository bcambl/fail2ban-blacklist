#!/usr/bin/python

import subprocess
import shlex
import csv

with open("/etc/fail2ban/blacklist.csv", "rb") as blacklist_file:
    blacklist = csv.DictReader(blacklist_file)
    for record in blacklist:
        cmd = str("iptables -I f2b-BLACKLIST 1 -s %s -j REJECT --reject-with "
                  "icmp-port-unreachable" % record['IP_ADDRESS'])
        subprocess.call(shlex.split(cmd))
