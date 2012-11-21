#!/usr/bin/python

import time
import gmail

mail = gmail.Gmail("username", "password")

while True:
	count = mail.count()
	print "Rich has " + str(count) + " new emails"

	time.sleep(60)