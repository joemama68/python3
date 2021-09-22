#!/usr/bin/env python3

import uuid

howmany = int(input("how many uuids to generate? "))

print("generating uuids  ")

for rando in range(howmany):
    print(uuid.uuid4())
