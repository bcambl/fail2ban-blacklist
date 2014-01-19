#!/usr/bin/python

from os import system


f = open("/etc/fail2ban/ip.blacklist", "r")
for i in f:
    system("fail2ban-client set ssh-iptables banip %s"% i)
f.close()
