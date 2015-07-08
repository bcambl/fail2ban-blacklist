# Persistent IP banning with Fail2ban

### Description

This project allows you to save all IP's that have been banned by fail2ban to a blacklist file via
some very basic python scripting.

Fail2ban will ban all ip's in the blacklist upon each restart. *(see: additional notes)*

### Installation

###### warning:
*If you have overridden actions.d/iptables.conf with a iptables.local file, Please review the iptables.local
file that is provided with this project and make the appropriate modifications to your version.*

After cloning this project:

````
cd fail2ban-blacklist
cp -r * /etc/fail2ban
````
Ensure blacklist.py and reban.py are executable:

```
chmod +x blacklist.py reban.py
```

Restart the fail2ban service: *(will vary base on your linux distribution)*

```
service fail2ban restart
```

### Usage

If the above installation instructions are followed, everything should work upon restarting fail2ban.

You can manually add IP's to the IP file:

```
/etc/fail2ban/blacklist.py <ip address>
```
The above command will add the IP to the ip.blacklist file if it does not already exist.

Re-banning of IP's is disabled by default. Un-comment the line in actions.d/iptables.d to enable.
You may also execute the reban.py script manually:
```
/etc/fail2ban/reban.py
```

#### optional:
Edit ```report.py``` with your email address and configure a cronjob to run daily.

copy ```report.py``` to ```/etc/cron.daily```

This will email you all the banned IP's from the previous day with the associated country code.

### Dependencies

Tested with python 2.7.9 on CentOS 6.6

##### Additional notes:

 - 1) If you are using the Fail2ban pyinotify functionality, Fail2ban will reban IP's when changes are
  detected in secure.log. This may create duplicate iptables entries for some IP's if reban is enabled.
