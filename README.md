#Persistent IP banning with Fail2ban
Added an action to run a script that logs banned IP's to a flat file (ip.blacklist)

Import IP's from ip.blacklist to Fail2ban by executing reban.py

######hint: Configure reban.py to when the fail2ban sevice starts
