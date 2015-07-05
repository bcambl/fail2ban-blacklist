#!/usr/bin/python

import subprocess
import shlex


f = open("/etc/fail2ban/ip.blacklist", "r")
for i in f:
    cmd = str("iptables -I f2b-BLACKLIST 1 -s %s "
              "-j REJECT --reject-with icmp-port-unreachable" % i)
    subprocess.call(shlex.split(cmd))
f.close()

