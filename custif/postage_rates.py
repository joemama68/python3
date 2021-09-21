#!/usr/bin/env python3

'''
    Calculate postage rates based on distance in miles
'''

distance = float(input("What is the distance in miles for the package to travel? "))

if distance < 2:
    message = 'The rate is $0.25'
elif distance < 10:
    message = 'The rate is $0.50'
elif distance < 50:
    message = 'The rate is $1.00'
elif distance > 50:
    message = 'The rate is $10.00'

print(message)
