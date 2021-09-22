#!/usr/bin/env python3

loginfail = 0

keystone_file = open("keystone.common.wsgi", "r")

for line in keystone_file:
    if "-] Authorization failed" in line:
        loginfail += 1

print("Failed logins: ",  loginfail)
keystone_file.close()
