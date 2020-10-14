#!/usr/bin/env python3

import sys, re
import argparse, requests
from nostril import nonsense

parser = argparse.ArgumentParser(description = "get js variable names from either a javascript file or a list of javascript urls.")

parser.add_argument('-u', '--url', default=False, action="store_true", help="Setting this will take a url or a list of urls from stdin, omitting it will take a javascript file on stdin.")
parser.add_argument('-s', '--smart', default=False, action="store_true", help="Smart detection tries to eliminate obfuscated/randomized variable names. This will give both false positives and false negatives, so use with caution")
args = parser.parse_args()

def read_in():
	# Read contents of stdin
	return [x.strip() for x in sys.stdin.readlines()]

def get_varnames(data):
	matches = []
	for match in re.findall(r' ([a-zA-Z0-9-_$]*) ?=', data):
		matches.append(match)
	return matches

params = set()

if args.url:
	urls_list = read_in()
	for url in urls_list:
		try:
			response = requests.get(url).text
			for match in get_varnames(response):
				params.add(match)
		except:
			pass
else:
	input_data = ' '.join(read_in())
	for match in get_varnames(input_data):
		params.add(match)



if args.smart:
	print('using smart detection')
	for param in params:
		regex = re.compile('[^a-zA-Z]') # pattern matches only alpha because nostril only works on alpha
		nostril_safe_param = regex.sub('', param) 
		if len(nostril_safe_param) > 6:
			if not nonsense(nostril_safe_param):
				print(param)
		else:
			print(param) # print everything under 7 chars, nostril won't work on anything shorter.

else:
	for param in params:
		print(param)
