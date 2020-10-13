#!/usr/bin/env python3

import sys, re

def read_in():
	# Read contents of stdin
	return [x.strip() for x in sys.stdin.readlines()]

input_data = ' '.join(read_in())

params = set()

for match in re.findall( r'([a-zA-Z0-9-_$]*) ?=', input_data):
	params.add(match)

for param in params:
	print(param)
