#!/usr/bin/env python3

import sys, re
import argparse, requests
from nostril import nonsense

parser = argparse.ArgumentParser(description = "get js variable names from either a javascript file or a list of javascript urls.")

parser.add_argument('-u', '--url', default=False, action="store_true", help="Setting this will take a url or a list of urls from stdin, omitting it will take a javascript file on stdin.")
parser.add_argument('-s', '--smart', default=False, action="store_true", help="User smart detection to eliminate obfuscated/randomized variable names. This will probably miss things")
args = parser.parse_args()

def read_in():
	# Read contents of stdin
	return [x.strip() for x in sys.stdin.readlines()]

def get_varnames(data):
	matches = []
	for match in re.findall(r'([a-zA-Z0-9-_$]*) ?=', data):
		matches.append(match)
	return matches

params = set()

if args.url:
	urls_list = read_in()
	for url in urls_list:
		try:
			response = requests.get(url).text
			for match in get_varnames(response):
				if args.smart and len(match) > 3:
					if not nonsense(match):
						params.add(match)
				else:
					params.add(match)
		except:
			pass
else:
	input_data = ' '.join(read_in())
	for match in get_varnames(input_data):
		if args.smart and len(match) > 3:
			if not nonsense(match):
				params.add(match)
		else:
			params.add(match)

for param in params:
	print(param)
