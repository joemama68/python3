#!/usr/bin/env python3

from subprocess import call

call(["ip", "link", "show", "up"])

print("check interfaces")

interface = input("Enter interface name: ")


call(["ip", "addr", "show", "dev", interface])

call(["ip", "route", "show", "dev", interface])
