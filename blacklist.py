#!/usr/bin/python

from datetime import datetime
from sys import argv
import csv
import re

ban_date = datetime.now().strftime('%Y-%m-%d')
ban_time = datetime.now().strftime('%H:%M-%S')


def ip_validation(ip=None):
    val = re.compile("^0*([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.0*"
                     "([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.0*"
                     "([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.0*"
                     "([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])$")
    if val.match(ip):
        return True
    else:
        print("Invalid IP: %s" % ip)


def ban_check(ip=None):
    if ip:
        with open("/etc/fail2ban/blacklist.csv", "rb") as blacklist_file:
            blacklist = csv.DictReader(blacklist_file)
            for record in blacklist:
                if ip in record['IP_ADDRESS']:
                    print("IP Already banned!")
                    return True


def ban(ip=None):
    if ip:
        with open("/etc/fail2ban/blacklist.csv", "ab") as blacklist_file:
            fieldnames = ['DATE', 'TIME', 'IP_ADDRESS']
            blacklist = csv.DictWriter(blacklist_file,
                                       delimiter=',',
                                       fieldnames=fieldnames)
            blacklist.writerow({'DATE': ban_date,
                                'TIME': ban_time,
                                'IP_ADDRESS': ip})


def main():
    try:
        ip = argv[1]
        if ip_validation(ip):
            if not ban_check(ip=ip):
                ban(ip)
    except IndexError:
        print("Please provide an IP to blacklist.")


if __name__ == '__main__':
    main()